
import RPi.GPIO as GPIO
import socket
from time import sleep  # Asegúrate de importar sleep

delay = 0.1
inPin = 40
outPin = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Configuración del socket
server_ip = '192.168.1.36'  # IP de tu PC
server_port = 5000           # Puerto a usar
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        readVal = GPIO.input(inPin)
        print(readVal)
        if readVal == 1:
            GPIO.output(outPin, 0)  # LED apagado
        if readVal == 0:
            GPIO.output(outPin, 1)  # LED encendido

        # Enviar el valor leído a la PC
        sock.sendto(str(readVal).encode(), (server_ip, server_port))
        sleep(delay)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO READY TO GO")

