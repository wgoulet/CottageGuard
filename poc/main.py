import picamera
from gpiozero import MotionSensor
import time
import math
import asyncio
import sys
import re

# Pre-reqs to get the GPIO inputs read 
#  pip install pigpio
#  sudo apt-get install pigpiod
#  sudo pigpiod

pir = MotionSensor(14)
pir.wait_for_motion()
print("Motion detected!")

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('my_video2.h264',quality=1)
camera.wait_recording(10)
camera.stop_recording()