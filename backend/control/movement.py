"""
Robot movement control module.

This module checks for movement commands and executes them
using GPIO pins (or prints to console for simulation).
"""

import time
# import RPi.GPIO as GPIO  # Uncomment this on Raspberry Pi
from config import MOTOR_LEFT_PIN, MOTOR_RIGHT_PIN

# Simulate GPIO setup for non-Raspberry Pi environments
class MockGPIO:
    BCM = "BCM"
    OUT = "OUT"
    HIGH = True
    LOW = False

    @staticmethod
    def setmode(mode):
        print(f"[GPIO] Set mode: {mode}")

    @staticmethod
    def setup(pin, mode):
        print(f"[GPIO] Setup pin {pin} as {mode}")

    @staticmethod
    def output(pin, state):
        print(f"[GPIO] Set pin {pin} to {'HIGH' if state else 'LOW'}")

# Replace with GPIO if running on real hardware
GPIO = MockGPIO  # Comment this line on Raspberry Pi

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_LEFT_PIN, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_PIN, GPIO.OUT)

# Global variable to store the current command
current_command = None

def set_command(cmd: str):
    """
    Set the current movement command (from outside).
    E.g., "forward", "backward", "left", "right", "stop"
    """
    global current_command
    current_command = cmd

def check_and_move():
    """
    This function is called in a loop.
    It reads the current_command and performs the corresponding action.
    """
    global current_command
    if current_command:
        print(f"[Movement] Executing command: {current_command}")
        if current_command == "forward":
            move_forward()
        elif current_command == "backward":
            move_backward()
        elif current_command == "left":
            turn_left()
        elif current_command == "right":
            turn_right()
        elif current_command == "stop":
            stop()
        current_command = None  # Clear after execution

def move_forward(duration=0.5):
    GPIO.output(MOTOR_LEFT_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT_PIN, GPIO.HIGH)
    time.sleep(duration)
    stop()

def move_backward(duration=0.5):
    GPIO.output(MOTOR_LEFT_PIN, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_PIN, GPIO.LOW)
    time.sleep(duration)
    stop()

def turn_left(duration=0.3):
    GPIO.output(MOTOR_LEFT_PIN, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_PIN, GPIO.HIGH)
    time.sleep(duration)
    stop()

def turn_right(duration=0.3):
    GPIO.output(MOTOR_LEFT_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT_PIN, GPIO.LOW)
    time.sleep(duration)
    stop()

def stop():
    GPIO.output(MOTOR_LEFT_PIN, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_PIN, GPIO.LOW)
