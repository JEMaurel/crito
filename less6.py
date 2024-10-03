#pull up  /mas led/ el script es el mismo 
#https://www.youtube.com/watch?v=0OYtR8UdZQk&list=PLGs0VKk2DiYxdMjCJmcP6jt4Yw6OHK85O&index=13

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
delay=.1
inPin=40
outPin=38
GPIO.setup(inPin,GPIO.IN)
GPIO.setup(outPin,GPIO.OUT)
from time import sleep
try:
	while True:
		readVal=GPIO.input(inPin)
		if readVal == 1:
			GPIO.output(outPin,0)
		if readVal ==0:
			GPIO.output(outPin,1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('thats all folks')



