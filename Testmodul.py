import pathlib
import shutil

def verarbeite():
    orig_file = pathlib.Path("/home/pi/Pictures/Aufnahme/image.jpg")
    copyto_file = pathlib.Path("/home/pi/Pictures/original/orig.jpg")
    orig_file.rename(copyto_file)