import lgpio
import time

PIN = 26
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h, PIN, lgpio.SET_PULL_UP)

try:
    while True:
        val = lgpio.gpio_read(h, PIN)
        print("🔍 État lu :", val)
        time.sleep(0.19)
except KeyboardInterrupt:
    lgpio.gpiochip_close(h)
    print("🛑 Fin")
