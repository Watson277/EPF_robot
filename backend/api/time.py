# time_api.py
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/time")
def get_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"time": now}