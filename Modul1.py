
from selenium import webdriver
#import urllib
from urllib.request import urlopen
import urllib.request
import msgpack

from selenium.webdriver.common.keys import Keys

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
word="strichmänchen"
url="http://images.google.com/search?q="+word+"&tbm=isch&sout=1"
driver.get(url)

url = deserialized_output['responseData']['results'][0]['unescapedUrl']
#imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
file = cStringIO.StringIO(urllib.urlopen(imageUrl).read())
img = Image.save("/home/pi/python_scripts/img.jpg")

#imageXpathSelector='//*[@id="ires"]/table/tbody/tr[1]/td[1]/a/img'
#img=driver.find_element_by_xpath(imageXpathSelector)
#src=(img.get_attribute('src'))
##urllib.urlretrieve(src, word+".jpg")
#urllib.request.urlretrieve(src, word+".jpg")
driver.close()
display.stop()