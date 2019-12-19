import pyautogui as pi, time

time.sleep (5)
pi.click()
distance = 400

while distance > 0:
	pi.dragRel(distance, 0 , duration=0.2) #move right
	distance = distance -50
	pi.dragRel( 0 ,distance, duration=0.2) #move down
	pi.dragRel(-distance, 0 , duration=0.2) #move left
	distance = distance -50
	pi.dragRel(0, -distance, duration=0.2) #move up
	
