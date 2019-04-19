from picamera import PiCamera
from time import sleep
import Testmodul

def takeapicture():

    camera = PiCamera()

    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Pictures/Aufnahme/image.jpg')
    camera.stop_preview()


Testmodul.verarbeite()