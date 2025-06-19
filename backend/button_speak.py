# button_reactor.py
import time
from api.voice_server import run_speech_once
from variables import button_state
print("run button service success")

def monitor_button_state():
    print("detect button state")
    print("val",button_state)
    if button_state == 1:  # Rising edge
        print("🔁 [button_reactor] Button state triggered!")
        run_speech_once()
    time.sleep(0.1)


