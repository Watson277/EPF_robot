# routes/dialog_api.py
from fastapi import APIRouter
import dialog_state

router = APIRouter()

@router.get("/latest")
def get_latest():
    return {
        "prompt": dialog_state.prompt_text,
        "response": dialog_state.response_text
    }
