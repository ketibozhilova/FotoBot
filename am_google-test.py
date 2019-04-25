
import requests
import re
from urllib import request 


filePath = '/home/pi/Pictures/original/original.jpg'
searchUrl = 'http://www.google.de/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']

#webbrowser.open(fetchUrl)
print (fetchUrl)


url_requ = request.urlopen(fetchUrl)
html_content = str(url_requ.read())
re_search_chunk = re.findall('<h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">.*?Mögliche verwandte Suchanfrage:', html_content)
print (re_search_chunk)