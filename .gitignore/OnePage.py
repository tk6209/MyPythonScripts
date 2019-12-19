#Dowload the dailyDashboard info


import time
import os
import glob
from selenium import webdriver
from subprocess import call


path = glob.glob("C:/Users/vteixeira/Downloads/*.csv")
for f in path:
    os.remove(f)


pref=webdriver.FirefoxProfile()
pref.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf,application/msword,application/csv,text/csv,application/rtf,application/xml,text/xml,application/octet-stream,application/vnd.ms-excel,application/zip,text/txt,text/plain,application/pdf,application/x-pdf")
pref.set_preference("browser.download.manager.showWenStarting",False)
pref.set_preference("browser.download.dir","C:/Users/vteixeira/tempAutomation/")
pref.set_preference("browser.download.folderList",2)
pref.set_preference("pdfjs.disabled",True)
#pref.set_preference("browser.download.fileName",)
ie = webdriver.Firefox(firefox_profile=pref)

username = 'vteixeira'
password = '0501Baruke'


ie.get('https://clientsupport.worldlinesweden.com/issues/?filter=-1')
ie.maximize_window()
username_button = ie.find_element_by_id ("login-form-username")
username_button.send_keys(username)
password_button = ie.find_element_by_id ("login-form-password")
password_button.send_keys(password)
login_button = ie.find_element_by_id ("login-form-submit")
login_button.click()
time.sleep(1)
ie.get('https://clientsupport.worldlinesweden.com/sr/jira.issueviews:searchrequest-csv-current-fields/11177/SearchRequest-11177.csv')
ie.quit()

call(["python", "os.py"])