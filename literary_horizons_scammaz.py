import pyautogui
import time

time.sleep(3)
a = 0

#has 305 pages

def tab():
	x = 988
	y = 604
	pyautogui.click(x=x, y=y, clicks=1, button='left') #clicks on site
	pyautogui.hotkey('ctrl', 'shift', 's') #screenshot page
	time.sleep(10) #wait to finish sc
	pyautogui.rightClick()
	time.sleep(0.1)
	pyautogui.click(x=x+54, y=y+86, clicks=1, button='left')
	time.sleep(1.5)

def word():
	pyautogui.click(x=1362, y=6, clicks=1, button='left') #go to word
	pyautogui.click(x=1859, y=1028, clicks=1, button='left') #click bot right word
	time.sleep(1)
	pyautogui.click(button='right') #clicks on site
	time.sleep(3)
	pyautogui.hotkey('k') #paste
	time.sleep(0.5)
	pyautogui.click(x=454, y=27, clicks=1, button='left') #click on tab
	pyautogui.click(x=707, y=85, clicks=1, button='left') #close new tab
	pyautogui.click(x=1810, y=674, clicks=1, button='left') #close new tab
	time.sleep(4)

while True:
	a += 1
	tab()
	word()
	if a == 280:
		break

print('stop')