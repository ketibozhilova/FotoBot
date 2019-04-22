
import requests


filePath = '/home/pi/Pictures/original/original.jpg'
searchUrl = 'http://www.google.hr/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
#webbrowser.open(fetchUrl)
print (fetchUrl)