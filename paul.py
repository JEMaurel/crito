

import RPi.GPIO as GPIO  # Importamos la librería RPi.GPIO
import time  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, 1)
on=True
off=False
GPIO.output(11,off)
time.sleep(3)
GPIO.output(11,on)
