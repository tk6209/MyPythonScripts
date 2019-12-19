import os, glob, time, xlrd 
from selenium import webdriver
import pyautogui as pi

ie = webdriver.Firefox()
target = ['']

    for target in target:
        ie.get(target)
        time.sleep(3)
        pi.press('enter')
        time.sleep(2)
        pi.press('enter')  

