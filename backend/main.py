import threading
import time
import asyncio
import uvicorn 
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from api.voice_server import run_speech_once
from button_speak import monitor_button_state
from api.time import router as time_router 
from api.time import router as time_router 
from api.api_server import router as dialog_router
from button_server import router as gpio_router
from api.speech_ws import router as speech_ws_router
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'control')))
from control import oeil

app = FastAPI()

# cross domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# mount api router
app.include_router(time_router)
app.include_router(gpio_router)
app.include_router(dialog_router)
app.include_router(speech_ws_router)

# WebSocket 
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")



# main fuction
if __name__ == "__main__":
    # start thread
    threading.Thread(target=oeil.action_clignement_repos, daemon=True).start()
    threading.Thread(target=monitor_button_state, daemon=True).start()
    # threading.Thread(target=run_adc_loop, daemon=True).start()
    #threading.Thread(target=run_speech_once, daemon=True).start()

    # start WebSocket process
    #threading.Thread(target=run_websocket_server, daemon=True).start()

    # start FastAPI HTTP service（main process）
    uvicorn.run(app, host="0.0.0.0", port=8000)


