
import urllib.request
import simplejson
import io
from PIL import Image

fetcher = urllib.build_opener()
searchTerm = 'parrot'
startIndex = 0
searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + startIndex
f = fetcher.open(searchUrl)
deserialized_output = simplejson.load(f)

imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
file = StringID.BytesIO(urllib.urlopen(imageUrl).read())
img = Image.save("/home/pi/python_scripts/img.jpg")