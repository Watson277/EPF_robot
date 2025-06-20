# button_reactor.py
import time
from api.voice_server import run_speech_once
import lgpio
import requests
import asyncio


print("run button service success")


def monitor_button_state():
    print("🔁 Monitoring button... (will exit on press)")
    while True:
        try:
            response = requests.get("http://localhost:8000/button")
            if response.status_code == 200:
                data = response.json()
                print("🟢 Button state:", data["state"])
                if data["state"] == 1:
                    run_speech_once()
                    print("✅ Button pressed! Exiting loop.")
                    

            else:
                print("❌ Failed to get button state")
        except Exception as e:
            print("❌ Error:", e)

        time.sleep(0.2)  # check every 200 ms


