import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Pines de los LEDs
rPin = 37
gPin = 35
bPin = 33

# Pines de los botones
rbut = 31  # Botón rojo
gbut = 29  # Botón verde

# Configurar pines de salida (LEDs)
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

# Configurar pines de entrada (Botones)
GPIO.setup(rbut, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gbut, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Configurar PWM para los LEDs
rPWM = GPIO.PWM(rPin, 1000)  # Frecuencia de 1 kHz
gPWM = GPIO.PWM(gPin, 1000)
bPWM = GPIO.PWM(bPin, 1000)

# Inicializar PWM con duty cycle al 0% (apagado)
rPWM.start(0)
gPWM.start(0)
bPWM.start(0)

def fade_in():
    """Incrementa la intensidad del LED rojo en 4 segundos de 0% a 100%"""
    for duty_cycle in range(0, 101):  # De 0 a 100%
        rPWM.ChangeDutyCycle(duty_cycle)
        time.sleep(4 / 100)  # 4 segundos para pasar de 0 a 100%

def sequence_lights():
    """Enciende los LEDs uno por uno y luego los apaga, repitiendo el ciclo"""
    gPWM.ChangeDutyCycle(100)  # Enciende LED verde
    time.sleep(1)  # Espera 1 segundo
    bPWM.ChangeDutyCycle(100)  # Enciende LED azul
    time.sleep(1)
    rPWM.ChangeDutyCycle(100)  # Enciende LED rojo
    time.sleep(1)
    
    # Apagar todos los LEDs
    rPWM.ChangeDutyCycle(0)
    gPWM.ChangeDutyCycle(0)
    bPWM.ChangeDutyCycle(0)
    time.sleep(1)

try:
    while True:
        # Si el botón rojo se presiona
        if GPIO.input(rbut) == GPIO.LOW:
            fade_in()

        # Si el botón verde se presiona
        if GPIO.input(gbut) == GPIO.LOW:
            sequence_lights()

        time.sleep(0.1)  # Pequeña pausa para evitar sobrecargar la CPU

except KeyboardInterrupt:
    pass

finally:
    # Apagar todos los LEDs y limpiar los pines GPIO
    rPWM.stop()
    gPWM.stop()
    bPWM.stop()
    GPIO.cleanup()
