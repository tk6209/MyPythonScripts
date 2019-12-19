import pyautogui,time
#time.sleep(5)


lista = ['Sometext','Gppi','Tortao','EUROBO']

#py.click(2560,0)


#execucao do codigo abaixo
pyautogui.click(700, 44,duration = 1.0)
pyautogui.typewrite("www.google.com")
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(1170, 406, duration = 1.0)

pyautogui.typewrite("pythonadddd")
pyautogui.press('enter')
pyautogui.alert('selecione o bloco de notas')
time.sleep(5)
pyautogui.doubleClick(312, 209)
pyautogui.hotkey('ctrl','c')
variavel = pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('alt','tab')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(2)

for  var in lista:
    pyautogui.doubleClick(593, 105, duration=0.5)
    pyautogui.click(593, 105)
    pyautogui.typewrite(var)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.doubleClick(312, 209)
    pyautogui.click(312, 209)
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')

pyautogui.alert('Encerrado')
