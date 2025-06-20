# gpio_router.py
from fastapi import APIRouter
import lgpio
from variables.button_state import button_val

router = APIRouter()
val = 0
# GPIO setup
PIN = 26
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h, PIN, lgpio.SET_PULL_UP)

@router.get("/button")
def read_button():

    """Returns the current state of the button."""
    button_val = lgpio.gpio_read(h, PIN)
    val = lgpio.gpio_read(h, PIN)
    #print("button_val",button_val)
    return {"state": button_val}
