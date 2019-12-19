import pyautogui as pi
import os, time, easygui, subprocess

activeUser = (os.getlogin())
winpath = ("C://WinAuth/WinAuth.exe")
ciscopath =("C://Program Files (x86)//Cisco//Cisco AnyConnect Secure Mobility Client//vpnui.exe")

def open_wAuth(winpath):
    return subprocess.Popen(winpath)

def close_wAuth(p):
    p.terminate()
    

def open_ciscoCon(ciscopath):
    return subprocess.Popen(ciscopath)

def close_ciscoCon(c):
    c.terminate()


print('Starting...')
p = open_wAuth(winpath)
time.sleep(3)

print('Loggin in on WinAuth... ')
#pass the credentials
pi.typewrite(os.environ.get('cred_winauth'))
pi.press('enter')
time.sleep(2)

print('Getting Current Code...')
#gets the current code
pi.hotkey('ctrl', '0')
time.sleep(2)

      
#initiate the AnnyConnect activity
print('Opening Cisco...')
c = open_wAuth(ciscopath)
time.sleep(2)
pi.hotkey('tab')
pi.hotkey('tab')
pi.hotkey('tab') 
pi.press('enter')
time.sleep(3)
print('Connecting...')

pi.typewrite(os.environ.get('cred_anyconn'))
pi.hotkey('tab')
pi.hotkey('ctrl', 'v')
pi.press('enter')


print('Check VPN status...')
time.sleep(3)
#closes winauth
close_wAuth(p)
#closes cisco
close_ciscoCon(c)



exit
