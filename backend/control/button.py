"""
Button control module.

This module checks GPIO input from physical buttons and triggers
corresponding actions such as toggling input mode, returning to home screen,
and toggling an LED light.
"""

import time
# import RPi.GPIO as GPIO  # Uncomment on Raspberry Pi
from config import BUTTON_SWITCH_INPUT_PIN, BUTTON_HOME_PIN, BUTTON_LED_PIN
from control import movement

# Simulated GPIO for testing without hardware
class MockGPIO:
    BCM = "BCM"
    IN = "IN"
    OUT = "OUT"
    HIGH = True
    LOW = False
    PUD_UP = "PUD_UP"

    pin_states = {
        BUTTON_SWITCH_INPUT_PIN: True,
        BUTTON_HOME_PIN: True,
        BUTTON_LED_PIN: True,
        18: False  # LED
    }

    @staticmethod
    def setmode(mode):
        print(f"[GPIO] Mode set to {mode}")

    @staticmethod
    def setup(pin, mode, pull_up_down=None):
        print(f"[GPIO] Pin {pin} set as {mode} with {pull_up_down}")

    @staticmethod
    def input(pin):
        return MockGPIO.pin_states[pin]

    @staticmethod
    def output(pin, value):
        MockGPIO.pin_states[pin] = value
        print(f"[GPIO] Pin {pin} output set to {'HIGH' if value else 'LOW'}")

GPIO = MockGPIO  # Comment this on real hardware

# LED pin
LED_PIN = 18

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_SWITCH_INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_HOME_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_LED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

# Debounce helper
last_pressed = {
    BUTTON_SWITCH_INPUT_PIN: 0,
    BUTTON_HOME_PIN: 0,
    BUTTON_LED_PIN: 0
}
DEBOUNCE_TIME = 0.3  # 300ms

def led_toggle():
    """
    Toggle LED ON/OFF.
    """
    current = GPIO.input(LED_PIN)
    GPIO.output(LED_PIN, not current)
    print(f"[Button] LED toggled to {'ON' if not current else 'OFF'}")

def listen_buttons():
    """
    Poll the button pins and execute actions on press (with debounce).
    Should be called periodically in a loop.
    """
    current_time = time.time()

    for pin in [BUTTON_SWITCH_INPUT_PIN, BUTTON_HOME_PIN, BUTTON_LED_PIN]:
        if GPIO.input(pin) == GPIO.LOW:
            if current_time - last_pressed[pin] > DEBOUNCE_TIME:
                handle_button_press(pin)
                last_pressed[pin] = current_time

def handle_button_press(pin):
    """
    Handle button logic for each pin.
    """
    if pin == BUTTON_SWITCH_INPUT_PIN:
        print("[Button] Switch input mode button pressed")
        # TODO: Add actual mode switch logic (e.g., set a global flag)
    elif pin == BUTTON_HOME_PIN:
        print("[Button] Home button pressed")
        # TODO: Implement return-to-home logic
        movement.set_command("stop")  # Example: stop robot
    elif pin == BUTTON_LED_PIN:
        print("[Button] LED toggle button pressed")
        led_toggle()
