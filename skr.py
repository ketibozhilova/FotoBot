import urllib.request
import random

url = "http://www.google.hr/search?tbs=sbi:AMhZZitWNvsjBGIx-Mzzjxhs3lFBCaMrQHNGtTJqU7uBR8IVX6J-7AuUec-sLw_1AcEht6fgxA4K1UMDlIXApfiGVjPVudHcmvqL6Kx0wK6YS-oSUXM9dpCQo9vbhnZgOqbFKAPVNvaQDZmBtck9JCjcotoIYqOgqihANcrbf260RxvooF4c2-LouAjlGYoV_1P5ogIXdS8SZMz4kgplRJFtkWwElAtonn1rg1wg0Bat3jAQXzlRI53Ub81fJzgZmFwQTJdaPb7BbmqKP7JpCQqH1sR4P5JBycSgtyYu7mQOI1Yewtkg0BCAmmTUaLFRoPI5Oxb9KEdodPREnY8UOe7m3AisFcvpnVcw"

def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)


downloader(url)