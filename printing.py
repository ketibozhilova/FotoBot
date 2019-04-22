
import cups
from PIL import Image
from tempfile import mktemp
from time import sleep

conn = cups.Connection()
printers = conn.getPrinters ()
prin = conn.getDefault()
myfile = "/home/pi/Pictures/aufnahme/test.txt"
conn.printFile (prin, myfile, "Project Report", {})