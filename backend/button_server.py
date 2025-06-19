# gpio_router.py
from fastapi import APIRouter
import lgpio
from variables import button_state

router = APIRouter()

# GPIO setup
PIN = 26
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h, PIN, lgpio.SET_PULL_UP)

@router.get("/button")
def read_button():
    """Returns the current state of the button."""
    button_state = lgpio.gpio_read(h, PIN)
    return {"state": button_state}
