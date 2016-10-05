from gpiozero import Servo
import time

servo = Servo (17)
servo.min()

time.sleep(1)
servo.mid()
time.sleep(1)
servo.max()


