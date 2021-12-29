from picamera import PiCamera, camera
from time import sleep

camera = PiCamera()
#while True:
camera.start_preview()
sleep(10)
camera.stop_preview()