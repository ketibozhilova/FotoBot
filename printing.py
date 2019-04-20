
import cups
from PIL import Image
from tempfile import mktemp
from time import sleep

conn = cups.Connection()
printers = conn.getPrinters ()
prin = conn.getDefault()
myfile = "/home/pi/Pictures/aufnahme/test.txt"
conn.printFile (prin, myfile, "Project Report", {})

## Set up CUPS
#conn = cups.Connection()
#printers = conn.getPrinters()
#printer_name = printers.keys()[0]
#cups.setUser('pi')

## Image (code taken from boothcam.py)
#im = Image.new('RGBA', (683, 384))
#im.paste(Image.open('/home/pi/Pictures/aufnahme/image.jpg').resize((683, 384)), ( 0, 0, 683, 384))

## Save data to a temporary file
#output = mktemp(prefix='jpg')
#im.save(output, format='jpeg')

## Send the picture to the printer
#print_id = conn.printFile(printer_name, output, "Photo Booth", {})
## Wait until the job finishes
#while conn.getJobs().get(print_id, None):
#    sleep(1)
#unlink(output)