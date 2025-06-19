import lgpio
import time

# === GPIO Pins ===
DIR_A = 17
ENA   = 18
DIR_B = 27
ENB   = 19

PWM_FREQ = 1000
VITESSE = 80

motor_value = 1

# === Initialisation GPIO ===
if motor_value:
    h = lgpio.gpiochip_open(0)

    for pin in [DIR_A, ENA, DIR_B, ENB]:
        lgpio.gpio_claim_output(h, pin)

# === Initialisation PWM ===
    lgpio.tx_pwm(h, ENA, PWM_FREQ, 0)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, 0)

# === Fonctions moteur ===
def avancer():
    print("➡️ Avancer")
    lgpio.gpio_write(h, DIR_A, 1)
    lgpio.gpio_write(h, DIR_B, 1)
    lgpio.tx_pwm(h, ENA, PWM_FREQ, VITESSE)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, VITESSE)
    time.sleep(2)
    stop()
    time.sleep(0.5)

def reculer():
    print("Reculer")
    lgpio.gpio_write(h, DIR_A, 0)
    lgpio.gpio_write(h, DIR_B, 0)
    lgpio.tx_pwm(h, ENA, PWM_FREQ, VITESSE)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, VITESSE)
    time.sleep(2)
    stop()
    time.sleep(0.5)

def gauche():
    print("Gauche")
    lgpio.gpio_write(h, DIR_A, 1)
    lgpio.gpio_write(h, DIR_B, 1)
    lgpio.tx_pwm(h, ENA, PWM_FREQ, 0)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, VITESSE)
    time.sleep(2)
    stop()
    time.sleep(0.5)

def droite():
    print("Droite")
    lgpio.gpio_write(h, DIR_A, 1)
    lgpio.gpio_write(h, DIR_B, 1)
    lgpio.tx_pwm(h, ENA, PWM_FREQ, VITESSE)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, 0)
    time.sleep(2)
    stop()
    time.sleep(0.5)

def stop():
    print("🛑 Stop")
    lgpio.tx_pwm(h, ENA, PWM_FREQ, 0)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, 0)
    lgpio.gpio_write(h, DIR_A, 0)
    lgpio.gpio_write(h, DIR_B, 0)

# === Programme principal ===
"""try:
    avancer(VITESSE)
    time.sleep(5)  # Avancer pendant 5 secondes
    stop()
    time.sleep(0.5)  # Petite pause pour bien observer l'arrêt
    reculer(VITESSE)
    time.sleep(5)  # Avancer pendant 5 secondes
    stop()
    time.sleep(0.5)
    gauche()
    time.sleep(5)  # Avancer pendant 5 secondes
    stop()
    time.sleep(0.5)
    droite()
    time.sleep(5)  # Avancer pendant 5 secondes
    stop()
    time.sleep(0.5)
finally:
    lgpio.gpiochip_close(h)
    print("✅ Terminé")"""
