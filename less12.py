import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

rPin = 37
gPin = 35
bPin = 33
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

rBut = 11
gBut = 13
bBut = 15

# Estados iniciales de los LEDs y botones
rLEDstate = 0
gLEDstate = 0
bLEDstate = 0

rButState = 1
gButState = 1
bButState = 1

rButStateOld = 1
gButStateOld = 1
bButStateOld = 1

GPIO.setup(rBut, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gBut, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bBut, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Leer el estado de los botones
        rButState = GPIO.input(rBut)
        gButState = GPIO.input(gBut)
        bButState = GPIO.input(bBut)

        # Detección de borde (de 1 a 0) para el botón rojo
        if rButState == 0 and rButStateOld == 1:  # Se detecta que el botón ha sido presionado
            rLEDstate = not rLEDstate  # Cambiar el estado del LED
            GPIO.output(rPin, rLEDstate)
            time.sleep(0.2)  # Pausa para evitar múltiples detecciones

        # Detección de borde (de 1 a 0) para el botón verde
        if gButState == 0 and gButStateOld == 1:
            gLEDstate = not gLEDstate
            GPIO.output(gPin, gLEDstate)
            time.sleep(0.2)

        # Detección de borde (de 1 a 0) para el botón azul
        if bButState == 0 and bButStateOld == 1:
            bLEDstate = not bLEDstate
            GPIO.output(bPin, bLEDstate)
            time.sleep(0.2)

        # Actualizar los estados anteriores de los botones
        rButStateOld = rButState
        gButStateOld = gButState
        bButStateOld = bButState

except KeyboardInterrupt:
    GPIO.cleanup()

