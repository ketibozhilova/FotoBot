from picamera import PiCamera
from time import sleep


def takeapicture():

    camera = PiCamera()

    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Pictures/Aufnahme/images.jpg')
    camera.stop_preview()

