from selenium import webdriver



filePath = "/home/pi/Pictures/original"


def searchfile():

        browser = webdriver.Firefox()

        browser.get('https://www.google.com/imghp?sbi=1')

        # Click "Search by image" icon
        elem = browser.find_element_by_class_name('gsst_a')
        elem.click()

        # Switch from "Paste image URL" to "Upload an image"
        browser.execute_script("google.qb.ti(true);return false")

        # Set the path of the local file and submit
        ele0 = browser.find_element_by_id("qbfile")
        ele0.send_keys(filePath)
        #  Clicking 'Visually Similar Images'
        ele1 = browser.find_element_by_link_text("Visually similar images")
        ele1.click()

        #  Selecting Image
        ele2 = browser.find_element_by_xpath("//div[@data-ri='0']/a")
        ele2.click()

        #  Getting the image URL
        ele3 = browser.find_element_by_link_text("View image")
        ele3.click()


        writeurl = open('imageurl.txt', 'w')
        browser.get(browser.current_url)
        print (browser.current_url)
        writeurl.close()
        browser.quit()

def searchurl():

        browser = webdriver.Firefox()
        url = open('imageurl.txt', 'r')
        url_contents = url.read()
        print (url_contents)
        url.close()

        browser.get(url_contents)

searchfile()
searchurl()