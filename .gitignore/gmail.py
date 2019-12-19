import sys
import os
import time

from selenium import webdriver
ie = webdriver.Firefox()
ie.maximize_window()
ie.get('https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/')


elmnt = ie.find_element_by_id('identifierId')
elmnt.send_keys('escudero.vinicius@gmail.com')
ie.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span').click()
time.sleep(2)

elmnt = ie.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/span/div[1]/div/div[1]/div/div[1]/input')
elmnt.send_keys('Baruke@01')
ie.find_element_by_id('passwordNext').click()
time.sleep(8)

##writeanewe-mail
ie.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div').click()
time.sleep(12)
##to
elmnt = ie.find_element_by_xpath('//*[@id=":191"]')
elmnt.send_keys('vinicius.escudero@outlook.com')

##subject
elmnt = ie.find_element_by_xpath('//*[@id=":18j"]')
elmnt.send_keys("send by my selenium PY scritp")

##body
elmnt = ie.find_element_by_xpath('//*[@id=":19o"]')
elmnt.send_keys(" esse eh o corpo do e-mail, tsc tsc tsc . . .")

##Send
elmnt = ie.find_element_by_xpath('//*[@id=":189"]').click()