from inputs import *
import sys

pad = devices.gamepads[0]
stick_max = 2.0**15

def kill(event):
	if event.state == 0:
		sys.exit()

def turn(event):
	if event.state > 0:
		print(':100 meters right 4', event.state/stick_max)
	else:
		print(':NASCAR', event.state/stick_max)

def gas(event):
	if event.state:
		print('Vroom')

def brake(event):
	if event.state:
		print('skreeeeeee')

def drift(event):
	if event.state:
		print('tokyo drift')

handler = {
	'ABS_X': turn,
	'BTN_START': kill,
	'BTN_EAST': brake,
	'BTN_SOUTH': gas,
	'ABS_Z': drift
}

while True:
	events = get_gamepad()
	for event in events:
			if event.code in handler:
				handler[event.code](event)
			# else:
			# 	print(event.ev_type, event.code, event.state)