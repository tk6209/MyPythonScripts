#Dowload the dailyDashboard info
from selenium import webdriver
import time
import sys
import io

#path = ("C:/Users/vteixeira/Desktop/Dashbord/One Page/")

pref=webdriver.FirefoxProfile()
pref.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf,")
pref.set_preference("browser.download.manager.showWenStarting",False)
pref.set_preference("browser.download.dir","C:/Users/vteixeira/Desktop/Dashbord/One Page/")
pref.set_preference("browser.download.folderList",2)
pref.set_preference("pdfjs.disabled",True)
#pref.set_preference("browser.download.fileName",)
browser = webdriver.Firefox(firefox_profile=pref)

browser.get('http://demo.automationtesting.in/FileDownload.html')
#browser.maximize_window()
browser.find_element_by_id("textbox").send_keys("testingtxt")
browser.find_element_by_id("createTxt").click()
browser.find_element_by_id("link-to-download").click()
print("TXT baixado")

time.sleep(1)

browser.get('http://demo.automationtesting.in/FileDownload.html')
#browser.maximize_window()
browser.find_element_by_id("pdfbox").send_keys("testingpdf")
browser.find_element_by_id("createPdf").click()
browser.find_element_by_id("pdf-link-to-download").click()
print("PDF baixado")


time.

print(browser.title)
# browser.quit()
