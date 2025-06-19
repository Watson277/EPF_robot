import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def send_max(register,data):
    spi.xfer2([register,data])

def clear():
    for i in range(1,9):
        send_max(i,0x00)

send_max(0x09,0x00)
send_max(0x0A,0x0F)
send_max(0x0B,0x07)
send_max(0x0C,0x01)
send_max(0x0F,0x00)

clear() 

time.sleep(0.5)

'''oeil_droit'''
patern1 =[0b01111110,
          0b11000011,
          0b10011001,
          0b10111101,
          0b10111101,
          0b10011001,
          0b11000011,
          0b01111110
          ]
'''oeil_transi_droit'''
patern2 =[0b01111110,
          0b11000011,
          0b10000001,
          0b11111001,
          0b11111001,
          0b10111001,
          0b11011011,
          0b01111110
          ]
'''oeil_transi_clignement'''
patern9 =[0b00111000,
          0b01000100,
          0b01011010,
          0b01111110,
          0b01111110,
          0b01011010,
          0b01000100,
          0b00111000
          ]
'''oeil_transi_clignement'''
patern10 =[0b00011000,
           0b00100100,
           0b00111100,
           0b00111100,
           0b00111100,
           0b00111100,
           0b00100100,
           0b00011000
          ]
'''oeil_transi_clignement'''
patern11 =[0b00011000,
           0b00111000,
           0b00111000,
           0b00111000,
           0b00111000,
           0b00111000,
           0b00111000,
           0b00011000
          ]
'''oeil croix'''
patern3 =[0b10000001,
          0b01000010,
          0b00100100,
          0b00011000,
          0b00011000,
          0b00100100,
          0b01000010,
          0b10000001
          ]
'''coeur'''
patern4 =[0b00001110,
          0b00011111,
          0b00111111,
          0b01111110,
          0b01111110,
          0b00111111,
          0b00011111,
          0b00001110
          ]
'''clignement d'oeil'''
patern5 =[0b00001000,
          0b00010000,
          0b00100000,
          0b00100000,
          0b00100000,
          0b00100000,
          0b00010000,
          0b00001000
          ]
'''clignement d'oeil haut'''
patern6 =[0b00100000,
          0b00010000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00010000,
          0b00100000
          ]
'''oeil bas droite'''
patern7 =[0b01111110,
          0b11000011,
          0b10000001,
          0b11110001,
          0b11111001,
          0b11111001,
          0b11111011,
          0b01111110
          ]
'''oeil haut gauche'''
patern8 =[0b01111110,
          0b11011111,
          0b10011111,
          0b10011111,
          0b10001111,
          0b10000001,
          0b11000011,
          0b01111110
          ]

def Croix():
        for i in range(1,9):
            send_max(i,patern3[i-1])
def milieu():
        for i in range(1,9):
            send_max(i,patern1[i-1])
def transi():
        for i in range(1,9):
            send_max(i,patern2[i-1])
def coeur():
        for i in range(1,9):
            send_max(i,patern4[i-1])
def clinB():
        for i in range(1,9):
            send_max(i,patern5[i-1])
def clinH():
        for i in range(1,9):
            send_max(i,patern6[i-1])
def droite():
        for i in range(1,9):
            send_max(i,patern7[i-1])
def gauche():
        for i in range(1,9):
            send_max(i,patern8[i-1])
def trans_clignement1():
        for i in range(1,9):
            send_max(i,patern9[i-1])
def trans_clignement2():
        for i in range(1,9):
            send_max(i,patern10[i-1])
def trans_clignement3():
        for i in range(1,9):
            send_max(i,patern11[i-1])
def regard_bas_droit():
    while True:
        time.sleep(1)
        milieu()
        time.sleep(0.1)
        transi()
        time.sleep(0.1)
        droite()
        time.sleep(3)
        transi()
        time.sleep(0.1)
        milieu()

def action_clignement_repos():
    while True:
        time.sleep(3)
        milieu()
        time.sleep(0.1)
        trans_clignement1()
        time.sleep(0.1)
        trans_clignement2()
        time.sleep(0.1)
        trans_clignement3()
        time.sleep(0.1)
        clinB()
        time.sleep(0.3)
        trans_clignement2() 
        time.sleep(0.1)
        trans_clignement1()   
        time.sleep(0.1)  
        milieu()






