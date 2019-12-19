import pyautogui as pi
import time

btn = ()

print('Starting CISCO the scritp ....')
time.sleep(1)

print('cisco open...')
btn = pi.locateOnScreen('C:/scripts/Py/pyautogui/cisco.png')
pi.click(btn,clicks=2)
time.sleep(2)



conn = pi.locateOnScreen('C:/scripts/Py/pyautogui/cisco.connected.png')
disconn = pi.locateOnScreen('C:/scripts/Py/pyautogui/cisco.disconnected.png')

if disconn is not None :

	print('Disconnected, connect ...')


elif conn is not None :
	print('Connected, pass ...')
	
else:
	print('Unkown error ...')
