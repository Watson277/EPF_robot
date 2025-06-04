# utils/command_parser.py

"""
Command parser module.

This module parses transcribed text from Whisper or text input,
determines if it contains robot movement commands, and returns
structured commands to be executed by the robot control module.
"""

import re

# Define a set of recognized commands and their canonical forms
COMMANDS = {
    "forward": ["forward", "go forward", "move forward", "前进", "往前走"],
    "backward": ["backward", "go backward", "move backward", "后退", "往后走"],
    "left": ["left", "turn left", "左转"],
    "right": ["right", "turn right", "右转"],
    "stop": ["stop", "halt", "停止", "停"],
}

def parse_command(text: str) -> dict | None:
    """
    Parses the input text to identify movement commands.

    Args:
        text (str): Transcribed text or input command.

    Returns:
        dict or None: Returns a dict with 'action' key if command recognized,
                      e.g., {'action': 'forward'}. Returns None if no command found.
    """
    text = text.lower()
    for action, keywords in COMMANDS.items():
        for kw in keywords:
            if kw in text:
                return {"action": action}
    return None

