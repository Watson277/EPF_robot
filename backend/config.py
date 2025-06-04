# config.py

"""
Configuration file for robot-backend project.

Contains all configurable parameters such as API URLs, hardware pins,
model paths, and other runtime settings.
"""

# FastAPI server config
HOST = "0.0.0.0"
PORT = 8000

# Whisper model configuration
WHISPER_MODEL_SIZE = "base"  # Options: tiny, base, small, medium, large

# LLM (local large language model) API configuration
LLM_API_URL = "http://localhost:1234/v1/chat/completions"
LLM_MODEL_NAME = "gpt-3.5-turbo"  # Replace with your model identifier

# Audio input config
AUDIO_INPUT_PATH = "temp.wav"  # Path to the audio file to transcribe

# Button GPIO pins (example, adjust per your hardware)
BUTTON_SWITCH_INPUT_PIN = 17
BUTTON_HOME_PIN = 27
BUTTON_LED_PIN = 22

# ADC related configuration
ADC_CHANNEL = 0  # ADC channel for battery voltage reading
VOLTAGE_REFERENCE = 3.3  # Reference voltage for ADC conversion

# Battery voltage to percentage conversion (example calibration)
BATTERY_VOLTAGE_MIN = 3.0
BATTERY_VOLTAGE_MAX = 4.2

# Movement control pins or interfaces
MOTOR_LEFT_PIN = 5
MOTOR_RIGHT_PIN = 6
# Add more pins or serial device names as needed

# WebSocket configuration
WEBSOCKET_HOST = "0.0.0.0"
WEBSOCKET_PORT = 8765
