import RPi.GPIO as GPIO
#import evdev
from evdev import InputDevice, categorize, ecodes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)


#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#button code variables (change to suit your device)
aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308
stpBtn = 311

#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == yBtn:
                GPIO.output(14,GPIO.HIGH)
		GPIO.output(15,GPIO.LOW)
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(23,GPIO.LOW)
            elif event.code == xBtn:
                GPIO.output(14,GPIO.LOW)
                GPIO.output(15,GPIO.LOW)
                GPIO.output(18,GPIO.HIGH)
                GPIO.output(23,GPIO.LOW)
            elif event.code == aBtn:
             	GPIO.output(14,GPIO.LOW)
                GPIO.output(15,GPIO.HIGH)
                GPIO.output(18,GPIO.LOW)
                GPIO.output(23,GPIO.HIGH)
            elif event.code == bBtn:
                GPIO.output(14,GPIO.HIGH)
                GPIO.output(15,GPIO.LOW)
                GPIO.output(18,GPIO.LOW)
                GPIO.output(23,GPIO.LOW)
	    elif event.code == stpBtn:
		GPIO.output(14,GPIO.LOW)
            	GPIO.output(15,GPIO.LOW)
            	GPIO.output(18,GPIO.LOW)
            	GPIO.output(23,GPIO.LOW)
	elif event.value == 0:
	    GPIO.output(14,GPIO.LOW)
            GPIO.output(15,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
