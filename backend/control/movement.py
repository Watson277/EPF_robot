
import pygame
import lgpio
import time

# === GPIO Pins ===
DIR_A = 17
ENA = 18
DIR_B = 27
ENB = 19
IR1_PIN = 22
IR2_PIN = 6
Trig_pin = 23
Echo_pin = 24

PWM_FREQ = 1000
VITESSE = 80

# === Initialisation GPIO ===
h = lgpio.gpiochip_open(0)

for pin in [DIR_A, ENA, DIR_B, ENB, Trig_pin]:
    lgpio.gpio_claim_output(h, pin)

for pin in [IR1_PIN, IR2_PIN, Echo_pin]:
    lgpio.gpio_claim_input(h, pin)

lgpio.tx_pwm(h, ENA, PWM_FREQ, 0)
lgpio.tx_pwm(h, ENB, PWM_FREQ, 0)

# === Fonctions moteurs ===
def avancer(vitesse=80):
    print("Avancer")
    lgpio.gpio_write(h, DIR_A, 1)
    lgpio.gpio_write(h, DIR_B, 1)
    lgpio.tx_pwm(h, ENA, PWM_FREQ, vitesse)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, vitesse)

def reculer(vitesse=80):
    print("Reculer")
    lgpio.gpio_write(h, DIR_A, 0)
    lgpio.gpio_write(h, DIR_B, 0)
    lgpio.tx_pwm(h, ENA, PWM_FREQ, vitesse)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, vitesse)

def gauche():
    print("Gauche")
    lgpio.gpio_write(h, DIR_A, 1)
    lgpio.gpio_write(h, DIR_B, 1)
    lgpio.tx_pwm(h, ENA, PWM_FREQ, 0)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, VITESSE)

def droite():
    print("Droite")
    lgpio.gpio_write(h, DIR_A, 1)
    lgpio.gpio_write(h, DIR_B, 1)
    lgpio.tx_pwm(h, ENA, PWM_FREQ, VITESSE)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, 0)

def stop():
    print("Stop")
    lgpio.tx_pwm(h, ENA, PWM_FREQ, 0)
    lgpio.tx_pwm(h, ENB, PWM_FREQ, 0)

# === Fonction distance ultrason ===
def distance():
    lgpio.gpio_write(h,  Trig_pin, 0)
    time.sleep(0.2)
    lgpio.gpio_write(h, Trig_pin , 1)
    time.sleep(0.2)
    lgpio.gpio_write(h, Trig_pin, 0)
    while lgpio.gpio_read(h, Echo_pin) == 0:
       pulse_start = time.time()
    while lgpio.gpio_read(h, Echo_pin)== 1:
       pulse_end = time.time()
    pulse_duration = pulse_end-pulse_start
    
    distance = (pulse_duration*34300)/2
    return distance

# === Initialisation Pygame ===
pygame.init()
screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption("Contrôle robot clavier")

try:
    print("🧠 Clavier + IR + Ultrason activé")

    while True:
        d = distance()
        print(f"📏 Distance mesurée : {d:.2f} cm")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise KeyboardInterrupt

            elif event.type == pygame.KEYDOWN:
                ir1 = lgpio.gpio_read(h, IR1_PIN)
                ir2 = lgpio.gpio_read(h, IR2_PIN)

                if event.key == pygame.K_UP:
                    if ir1 == 0 and d > 10:
                        avancer(VITESSE)
                    else:
                        print("❌ Avancer interdit (vide ou obstacle)")
                        stop()

                elif event.key == pygame.K_DOWN:
                    if ir2 == 0:
                        reculer(VITESSE)
                    else:
                        print("❌ Reculer interdit (vide détecté)")
                        stop()

                elif event.key == pygame.K_LEFT:
                    if ir1 == 0 and ir2 == 0 and d > 10:
                        gauche()
                    else:
                        print("❌ Tourner gauche interdit (vide ou obstacle)")
                        stop()

                elif event.key == pygame.K_RIGHT:
                    if ir1 == 0 and ir2 == 0 and d > 10:
                        droite()
                    else:
                        print("❌ Tourner droite interdit (vide ou obstacle)")
                        stop()

                elif event.key == pygame.K_ESCAPE:
                    print("🚪 Fermeture demandée (ESC)")
                    raise KeyboardInterrupt

            elif event.type == pygame.KEYUP:
                stop()

        time.sleep(0.05)

except KeyboardInterrupt:
    print("🛑 Interruption manuelle.")

finally:
    stop()
    lgpio.gpiochip_close(h)
    pygame.quit()
