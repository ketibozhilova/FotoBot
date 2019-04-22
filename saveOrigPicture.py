def verarbeite():

    import pathlib
    import os
   
    pfad = "/home/pi/Pictures/original/"
    dateien = os.listdir(pfad)
    anzahl = len(dateien)
            
    orig_file = pathlib.Path("/home/pi/Pictures/aufnahme/image.jpg")
    copyto_file = pathlib.Path("/home/pi/Pictures/original/original.jpg")
    orig_file.rename(copyto_file)
