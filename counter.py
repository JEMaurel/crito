import RPi.GPIO as GPIO
import time

# Configuramos el modo de los pines para usar la numeración física de los pines (BOARD)
GPIO.setmode(GPIO.BOARD)

# Configuramos el pin 11 como salida
GPIO.setup(11, GPIO.OUT)

# Pedimos al usuario cuántas veces desea que parpadeen las luces
numBlinks = int(input("¿Cuántas veces deseas que parpadeen las luces? "))

# Bucle para encender y apagar el pin
for i in range(numBlinks):
    GPIO.output(11, 1)  # Enciende el pin
    time.sleep(1)          # Espera 1 segundo
    GPIO.output(11, 0) # Apaga el pin
    time.sleep(1)          # Espera 1 segundo

# Limpieza de los pines al final
GPIO.cleanup()

