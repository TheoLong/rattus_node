import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
def moveRight(velocity):
	print("move right")
	power=0.0
	power=velocity*7
	if power>100.0:
		power=100.0
	if power <-100.0:
		power=-100.0
	power=round(power,0)
	power=int(power)
	#if power > 0, moving forward
	if power>0:
                GPIO.output("P9_11", GPIO.HIGH);
                GPIO.output("P9_12", GPIO.LOW);
                PWM.set_duty_cycle("P9_14",power)
	#if power < 0, move backward
	if power<0:
		power=abs(power)
		GPIO.output("P9_11", GPIO.LOW);
                GPIO.output("P9_12", GPIO.HIGH);
                PWM.set_duty_cycle("P9_14",power)
	#if power = 0, stop
	if power == 0:
		GPIO.output("P9_11", GPIO.LOW);
                GPIO.output("P9_12", GPIO.LOW);
                PWM.set_duty_cycle("P9_14",0)
def moveLeft(velocity):
	print("move left")
	power=0.0
	power=velocity*7
	if power>100.0:
		power=100.0
	if power <-100.0:
		power=-100.0
	power=round(power,0)
	power=int(power)
	#if power > 0, moving forward
	if power>0:
                GPIO.output("P9_13", GPIO.HIGH);
                GPIO.output("P9_15", GPIO.LOW);
                PWM.set_duty_cycle("P9_16",power)
	#if power < 0, move backward
	if power<0:
		power=abs(power)
		GPIO.output("P9_15", GPIO.LOW);
                GPIO.output("P9_15", GPIO.HIGH);
                PWM.set_duty_cycle("P9_16",power)
	#if power = 0, stop
	if power == 0:
		power=round(power)
		GPIO.output("P9_13", GPIO.LOW);
                GPIO.output("P9_15", GPIO.LOW);
                PWM.set_duty_cycle("P9_16",0)
		

