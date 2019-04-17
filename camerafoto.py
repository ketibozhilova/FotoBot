from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Pictures/Aufnahme/image%s.jpg')
camera.stop_preview()