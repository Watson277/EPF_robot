
from fastapi import APIRouter
import variables.dialog_state as dialog_state

router = APIRouter()

@router.get("/latest")
def get_latest():
    return {
        "prompt": dialog_state.prompt_text,
        "response": dialog_state.response_text
    }