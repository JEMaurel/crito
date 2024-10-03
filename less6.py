#pull up / down / etc ver commits 
#https://www.youtube.com/watch?v=0OYtR8UdZQk&list=PLGs0VKk2DiYxdMjCJmcP6jt4Yw6OHK85O&index=13

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
inPin=40
GPIO.setup(inPin,GPIO.IN)
from time import sleep
try:
	while True:
		readVal=GPIO.input(inPin)
		print(readVal)
		sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()

