#https://www.youtube.com/watch?v=yL5BNA_Ex6s&list=PLGs0VKk2DiYxdMjCJmcP6jt4Yw6OHK85O&index=13
# toggle button

from time import sleep
import RPi.GPIO as GPIO
delay = .1
inPin =40
outPin= 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
LEDstate=0
buttonState=1
buttonStateOld=1
try:
	while True:
		buttonState=GPIO.input(inPin)
		print(buttonState)
		if  buttonState ==0 and buttonStateOld ==1 :
			LEDstate = not LEDstate
			GPIO.output(outPin,LEDstate)
		buttonStateOld=buttonState
		sleep(delay) 



except KeyboardInterrupt:
	GPIO.cleanup()
	print('gpio good to go') 
