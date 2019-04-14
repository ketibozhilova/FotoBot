from picamera import PiCamera
from time import sleep


def takeapicture():

    camera = PiCamera()

    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Pictures/Aufnahme/image.jpg')
    camera.stop_preview()

