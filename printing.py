
import cups
from PIL import Image
from tempfile import mktemp
from time import sleep

import pathlib
import os


def toprint(pathtosave):
    conn = cups.Connection()
    printers = conn.getPrinters ()
    prin = conn.getDefault()
    myfile = pathtosave
    #conn.printFile (prin, myfile, "Project Report", {})

    pfad = "/home/pi/Pictures/save/"
    dateien = os.listdir(pfad)
    anzahl = len(dateien)
            
    orig_file = pathlib.Path(pathtosave)
    copyto_file = pathlib.Path("/home/pi/Pictures/save/save-" + str(int(anzahl + 1)) + ".jpg")
    orig_file.rename(copyto_file)

    #deleting files
    if os.path.exists("/home/pi/Pictures/merge-to-print/merge.jpg"):
        os.remove("/home/pi/Pictures/merge-to-print/merge.jpg")
    else: print("merge.jpg not found")

    if os.path.exists("/home/pi/Pictures/original/original.jpg"):
        os.remove("/home/pi/Pictures/original/original.jpg")
    else: print("original.jpg not found")

    if os.path.exists("/home/pi/Pictures/erhalten/abgeholt.jpg"):
        os.remove("/home/pi/Pictures/erhalten/abgeholt.jpg")
    else: print("abgeholt.jpg not found")

#def toprint():
#    # Set up CUPS
#    conn = cups.Connection()
#    printers = conn.getPrinters ()
#    printer_name = conn.getDefault()
#    cups.setUser('pi')

#    # Image (code taken from boothcam.py)
#    im = Image.new('RGBA', (683, 384))
#    im.paste(Image.open('home/pi/Pictures/merge-to-print/Trifecta.jpg').resize((683, 384)), ( 0, 0, 683, 384))

#    # Save data to a temporary file
#    output = mktemp(prefix='jpg')
#    im.save(output, format='jpeg')

#    # Send the picture to the printer
#    print_id = conn.printFile(printer_name, output, "Photo Booth", {})
#    # Wait until the job finishes
#    while conn.getJobs().get(print_id, None):
#        sleep(1)
#    unlink(output)