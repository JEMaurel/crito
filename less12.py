

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

rPin = 37
gPin = 35
bPin = 33
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

# Configurar PWM para los pines de los LEDs
rPWM = GPIO.PWM(rPin, 1000)  # Frecuencia de 1 kHz
gPWM = GPIO.PWM(gPin, 1000)
bPWM = GPIO.PWM(bPin, 1000)

# Inicializar PWM con duty cycle al 0% (apagado)
rPWM.start(0)
gPWM.start(0)
bPWM.start(0)

rBut = 11
gBut = 13
bBut = 15

# Estados iniciales de los LEDs y botones
rButState = 1
gButState = 1
bButState = 1

rButStateOld = 1
gButStateOld = 1
bButStateOld = 1

# Contadores de intensidad (de 0 a 10)
rIntensity = 0
gIntensity = 0
bIntensity = 0

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
        if rButState == 0 and rButStateOld == 1:
            rIntensity = (rIntensity + 1) % 11  # Incrementar intensidad y reiniciar a 0 después de 10
            rPWM.ChangeDutyCycle(rIntensity * 10)  # Convertir la intensidad a ciclo de trabajo (0-100%)
            time.sleep(0.2)  # Pausa para evitar múltiples detecciones

        # Detección de borde (de 1 a 0) para el botón verde
        if gButState == 0 and gButStateOld == 1:
            gIntensity = (gIntensity + 1) % 11
            gPWM.ChangeDutyCycle(gIntensity * 10)
            time.sleep(0.2)

        # Detección de borde (de 1 a 0) para el botón azul
        if bButState == 0 and bButStateOld == 1:
            bIntensity = (bIntensity + 1) % 11
            bPWM.ChangeDutyCycle(bIntensity * 10)
            time.sleep(0.2)

        # Actualizar los estados anteriores de los botones
        rButStateOld = rButState
        gButStateOld = gButState
        bButStateOld = bButState

except KeyboardInterrupt:
    rPWM.stop()
    gPWM.stop()
    bPWM.stop()
    GPIO.cleanup()
