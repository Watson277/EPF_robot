# """
# Battery ADC module.

# This module reads the battery voltage using ADC (Analog to Digital Converter)
# and calculates the remaining battery percentage.
# """

# import time
# import spidev  # Uncomment when using hardware SPI on Raspberry Pi
# import RPi.GPIO as GPIO
# import random  # For simulation without hardware

# # SPI configuration (for real ADC like MCP3008)
# spi = spidev.SpiDev()
# spi.open(0, 0)
# spi.max_speed_hz = 1350000

# # Voltage reference and battery parameters
# VREF = 3.3  # Reference voltage for ADC
# BATTERY_FULL = 4.2
# BATTERY_EMPTY = 3.3

# def read_adc_channel(channel=0):
#     """
#     Read ADC value from the specified channel.
#     Replace with real SPI code when on hardware.
#     """
#     # Real SPI read example (for MCP3008):
#     adc = spi.xfer2([1, (8 + channel) << 4, 0])
#     value = ((adc[1] & 3) << 8) + adc[2]
#     voltage = value * VREF / 1023
#     return voltage

#     # Simulated voltage for testing
#     voltage = random.uniform(3.3, 4.2)      
#     return round(voltage, 2)

# def calculate_percentage(voltage):
#     """
#     Convert voltage to battery percentage.
#     """
#     if voltage >= BATTERY_FULL:
#         return 100
#     elif voltage <= BATTERY_EMPTY:
#         return 0
#     else:
#         return int(((voltage - BATTERY_EMPTY) / (BATTERY_FULL - BATTERY_EMPTY)) * 100)

# def read_battery():
#     """
#     Main function to read battery voltage and calculate power level.
#     Call this periodically in a background thread.
#     """
#     voltage = read_adc_channel()
#     percent = calculate_percentage(voltage)
#     print(f"[ADC] Battery voltage: {voltage:.2f}V ({percent}%)")

#     # TODO: Send battery info to frontend or global state if needed
#     # Example: websocket_manager.broadcast({"type": "battery", "voltage": voltage, "percent": percent})
