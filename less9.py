
#  aqui paul lo hizo en el shell pero bue aca meti algo con la ia 


import RPi.GPIO as GPIO

# Desactivar advertencias si el canal ya está en uso
GPIO.setwarnings(False)

# Configurar el modo de los pines
GPIO.setmode(GPIO.BOARD)

# Configurar el pin 12 (GPIO 18) como salida
GPIO.setup(12, GPIO.OUT)

# Configurar PWM en el pin 12 con una frecuencia de 1000 Hz
myPWM = GPIO.PWM(12, 99)

# Iniciar PWM con un ciclo de trabajo del 50%
myPWM.start(1)

try:
    # Mantener el programa en ejecución
    while True:
        pass  # El LED permanecerá encendido al 50% de brillo

except KeyboardInterrupt:
    # Detener el PWM al recibir una interrupción del teclado (Ctrl+C)
    myPWM.stop()
    GPIO.cleanup()  # Limpiar configuración GPIO
