import urllib.request
import random

image_url = "http://www.google.com.au/imghp"

def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)


downloader(image_url)