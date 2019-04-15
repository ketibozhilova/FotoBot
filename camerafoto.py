from picamera import PiCamera
from time import sleep
from pathlib import Path


def takeapicture():

    i = 0

    camera = PiCamera()
    camera.start_preview()
    
    MyPicture = Path("/home/pi/Pictures/Aufnahme/image" + str(i) + ".jpg")

    if MyPicture.is_file():
        while i > i:
            i += 1
    MyPicture = Path("/home/pi/Pictures/Aufnahme/image" + str(i) + ".jpg")

    camera.capture('/home/pi/Pictures/Aufnahme/image.jpg')
    camera.stop_preview()

