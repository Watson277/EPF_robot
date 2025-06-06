## Project Architecture
```
                                                ┌────────────────────────────────────────────────────────┐
                                                │                    robot-backend (FastAPI)             │
                                                │                                                        │
                                                │  ┌────────────┐     ┌──────────────┐     ┌────────────┐│
                                                │  │ Whisper    │     │LLM (LMStudio)│     │ WebSocket  ││
                                                │  │ 语音识别    │     │ 语言模型对话  │     │ 与前端通信  ││
                                                │  │ whisper_module.py│ chat.py      │     │ server.py  ││
                                                │  └────────────┘     └──────────────┘     └────────────┘│
                                                │         │                   ▲                 ▲        │
                                                │         ▼                   │                 │        │
                                                │  ┌────────────────────────────────────────────┐        │
                                                │  │         指令解析器 command_parser.py        │        │
                                                │  └────────────────────────────────────────────┘        │
                                                │         │                                              │
                                                │         ▼                                              │
                                                │  ┌─────────────────────┐      ┌─────────────────────┐  │
                                                │  │ movement.py         │      │ button.py           │  │
                                                │  │ 控制机器人运动       │      │ 控制页面与功能按钮    │  │
                                                │  └─────────────────────┘      └─────────────────────┘  │
                                                │         ▲                              ▲               │
                                                │         │                              │               │
                                                │         ▼                              ▼               │
                                                │  ┌─────────────────────┐              ┌──────────────┐ │
                                                │  │ adc.py              │              │ Frontend Web │ │
                                                │  │ 电压读取 → 电量计算  │              │ 实时显示状态  │  │
                                                │  └─────────────────────┘              └──────────────┘ │
                                                │                                                        │
                                                │         （多线程协同运行 - main.py）                     │
                                                └────────────────────────────────────────────────────────┘
```


---

## 3. Module Roles and Running Logic

### 3.1 WebSocket Server (`\server.py`)

- Implements an asynchronous WebSocket server listening for frontend connections.
- Pushes battery status updates every 5 seconds to all connected clients.
- Receives robot movement commands (e.g., "forward", "left") and delegates to the movement module.
- Handles chat messages, forwarding them to the LLM backend (integration point).
- Manages connected client sessions and error handling.

### 3.2 Battery Monitor (`control/adc.py`)

- Interfaces with an SPI ADC (e.g., MCP3008) to read the battery voltage from hardware.
- Converts raw ADC values to voltage, then calculates battery percentage based on configured min/max voltage.
- Periodically polls battery voltage and exposes the current battery level.
- Used by WebSocket server to broadcast battery status to frontend clients.

### 3.3 Robot Movement Controller (`control/movement.py`)

- Controls motor drivers via GPIO pins on the Raspberry Pi.
- Executes movement commands received from the WebSocket server or other modules.
- Supports commands such as forward, backward, left, right, and stop.
- Encapsulates hardware-specific control logic for robot movement.

### 3.4 Button Listener (`control/button.py`)

- Listens to physical button GPIO inputs with debounce handling.
- Handles UI-related actions triggered by button presses:
  - Switch input modes (e.g., keyboard vs. voice)
  - Return to home screen
  - Toggle LED on/off
- Runs as a separate thread or process, continuously monitoring button states.
- Updates system state or notifies other modules as needed.

### 3.5 Whisper Speech Recognition Module (`modules/whisper_module.py`)

- Loads the Whisper ASR model to convert audio input into text commands.
- Audio input can be from microphone recordings saved as temporary files.
- Transcribed text is parsed for movement or chat commands.
- Integrated with the LLM backend or command parser to trigger robot actions.

### 3.6 Large Language Model Backend (Custom Integration)

- Receives user chat input (from WebSocket or local interface).
- Generates natural language responses or interprets complex commands.
- Works alongside the Whisper ASR module and frontend chat UI.
- Can run locally or connect to cloud LLM services depending on deployment.

### 3.7 REST API Server (Optional)

- Implemented with FastAPI to provide extensible REST endpoints.
- Enables external services or frontend to fetch robot status or send commands.
- Runs concurrently with WebSocket and button listener modules.

---

## 4. Main Runtime Flow (`main.py`)

- Starts the button listener in a dedicated thread to monitor physical button inputs.
- Launches the WebSocket server asynchronously in the main thread to handle frontend communication.
- Runs the REST API server in a background thread (optional, can be disabled if not used).
- Coordinates communication between modules:
  - Button presses trigger UI mode changes or LED control.
  - Battery monitor updates are pushed via WebSocket.
  - Movement commands come from WebSocket and/or voice recognition.
  - Voice input is transcribed and parsed to generate commands or chat messages.

---

## 5. Summary of Inter-Module Communication

| Sender/Trigger            | Receiver/Effect                      | Communication Method        |
|--------------------------|------------------------------------|-----------------------------|
| Frontend UI              | WebSocket server                   | WebSocket message            |
| WebSocket server         | Movement controller                | Direct function call or GPIO control |
| WebSocket server         | Frontend UI                       | WebSocket push updates (battery, chat) |
| ADC battery monitor      | WebSocket server                   | Function call / shared state |
| Button listener          | System state / UI mode             | Shared state or event flags  |
| Whisper ASR              | LLM backend / command parser       | Function calls / API         |
| LLM backend              | WebSocket server                   | Function call or async events|

---

## 6. How to Run

1. Setup Raspberry Pi with required hardware and permissions.
2. Create and activate Python virtual environment.
3. Install dependencies via `pip install -r requirements.txt`.
4. Configure `config.py` for your hardware GPIO pins and parameters.
5. Run the project entry point:

```bash
python main.py

