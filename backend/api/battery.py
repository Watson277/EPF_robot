# battery/routes.py

from fastapi import APIRouter
import board
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

router = APIRouter()

# 初始化 ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
ads.gain = 1
chan = AnalogIn(ads, ADS1115.P0)

# 电池参数
VOLTAGE_DIVIDER_RATIO = 2.0
BATTERY_FULL = 4.2
BATTERY_EMPTY = 3.0

def get_battery_voltage():
    return chan.voltage * VOLTAGE_DIVIDER_RATIO

def get_battery_percentage(voltage):
    if voltage >= BATTERY_FULL:
        return 100
    elif voltage <= BATTERY_EMPTY:
        return 0
    else:
        return int((voltage - BATTERY_EMPTY) / (BATTERY_FULL - BATTERY_EMPTY) * 100)

@router.get("/battery")
def battery_info():
    voltage = get_battery_voltage()
    percent = get_battery_percentage(voltage)
    return {
        "voltage": round(voltage, 2),
        "percentage": percent
    }
