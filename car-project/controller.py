from inputs import *
import sys
from gpiozero import AngularServo
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit

mh = Adafruit_MotorHAT(addr=0x60)
leftMotor = mh.getMotor(4)
#rightMotor = mh.getMoto(3)

servo = AngularServo(
	pin=17,
	min_pulse_width = .0008,
	max_pulse_width = .0018,
	min_angle = -60,
	max_angle = 60
)

pad = devices.gamepads[0]
stick_max = 2.0**15

def turnoffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnoffMotors)

def turn(event):
	if abs(event.state/stick_max) < .15:
		servo.angle = 0
	else:
		servo.angle = -servo.min_angle*event.state/stick_max
	
	if event.state > 0:
		print('right', event.state/stick_max)
	else:
		print('left', event.state/stick_max)

def kill(event):
	if event.state == 0:
		sys.exit()

def gas(event):
	if event.state:
		print('Vroom')

def brake(event):
	if event.state:
		print('skreeeeeee')

def drift(event):
	if event.state:
		print('tokyo drift')

def forward(event):
	if event.state:
		print("forward",event.state)
		leftMotor.run(Adafruit_MotorHAT.FORWARD)
#		rightMotor.run(Adafruit_MotorHAT.FORWARD)
		leftMotor.setSpeed(100)
#		rightMotor.setSpeed(event.state)

def backward(event):
	if event.state:
		print("backward",event.state)

handler = {
	'ABS_X': turn,
	'BTN_START': kill,
	'BTN_EAST': brake,
	'BTN_SOUTH': gas,
#	'ABS_Z': drift,
	'ABS_RZ': forward,
#	'ABS_Z': backward
}

# servo.mid()

#print('frame_width:', servo.frame_width)
#print('pulse_width:', servo.pulse_width)
#print('max_pulse_width:', servo.max_pulse_width)
#print('min_pulse_width:', servo.min_pulse_width)
#print('source:', servo.source)
#print('source_delay:', servo.source_delay)

while True:
	events = get_gamepad()
	for event in events:
			if event.code in handler:
				handler[event.code](event)
#	 		else:
#	 		 	print(event.ev_type, event.code, event.state)
