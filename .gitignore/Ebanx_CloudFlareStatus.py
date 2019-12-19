#!/usr/bin/env python
import time
import datetime
from selenium import webdriver


ie = webdriver.Firefox()
ie.set_window_size(0,0)
ie.get('https://www.cloudflarestatus.com/?_ga=2.32235838.1625635847.1562077657-1827693440.1562077657')

time.sleep(5)
print('\n','\n',ie.title)
print('  Start time: ',datetime.datetime.now())
print ('\n',ie.current_url)

btn =  ie.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/div[1]/span[1]/span[2]')
btn.click()

btn = ie.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/span[1]')
print (btn.text)

stk = ie.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[39]/span[2]')
print ('  Stockholm, Sweden - (ARN) is:', stk.text)

got = ie.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[16]/span[2]')
print ('  Gothenburg, Sweden - (GOT) is:', got.text)

cwb = ie.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/div[2]/div[4]/span[2]')
print ('  Curitiba, Brazil - (CWB) is:', cwb.text)

gru = ie.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/div[2]/div[13]/span[2]')
print ('  São Paulo, Brazil - (GRU) is:', gru.text)

print('\n','\n','End time: ', datetime.datetime.now())

ie.quit()

