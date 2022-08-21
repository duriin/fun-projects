import pyautogui
import time

print(pyautogui.position())
time.sleep(2)

x = 0

while True:
	pyautogui.click(x=-1456, y=315, clicks=1, button='left')
	pyautogui.click(x=-1020, y=407, clicks=1, button='left')
	time.sleep(0.5)
	pyautogui.moveTo(x=-1482, y=504)
	pyautogui.dragTo(x=-960, y=1260, duration=0.1)
	pyautogui.hotkey('ctrl', 'c')
	pyautogui.click(x=-1639, y=362, clicks=1, button='left')
	#pyautogui.click(x=-831, y=1327, clicks=1, button='left')
	pyautogui.hotkey('ctrl', 'v')
	#pyautogui.click(x=-1177, y=779, clicks=1, button='left')
	#time.sleep(0.5)
	#pyautogui.click(x=-85, y=612, clicks=1, button='left')
	#time.sleep(0.1)
	#pyautogui.click(x=-818, y=1351, clicks=1, button='left')
	#pyautogui.hotkey('enter')
	#pyautogui.scroll(-1000)

	pyautogui.click(x=-1806, y=354, clicks=1, button='left')
	pyautogui.click(x=-1456, y=315, clicks=1, button='left')
	pyautogui.click(x=-1544, y=410, clicks=1, button='left')
	time.sleep(0.5)
	pyautogui.moveTo(x=-960, y=504)
	pyautogui.dragTo(x=-438, y=1260, duration=0.1)
	pyautogui.hotkey('ctrl', 'c')
	pyautogui.click(x=-1639, y=362, clicks=1, button='left')
	#pyautogui.click(x=-831, y=1327, clicks=1, button='left')
	pyautogui.hotkey('ctrl', 'v')
	#pyautogui.click(x=-1177, y=779, clicks=1, button='left')
	#time.sleep(0.5)
	#pyautogui.click(x=-85, y=612, clicks=1, button='left')
	#time.sleep(0.1)
	#pyautogui.click(x=-818, y=1351, clicks=1, button='left')
	#pyautogui.hotkey('enter')
	#pyautogui.scroll(-1000)
	pyautogui.click(x=-1806, y=354, clicks=1, button='left')
	pyautogui.click(x=-28, y=911, clicks=1, button='left')
	time.sleep(1)

	x += 1
	if x == 130:
		break
 
print('end')

'''
snipping app: x=-1456, y=315
snipping 1: x=-1544, y=410
snipping 2: x=-1021, y=410

page 1 top L: x=-1482, y=504
page 1 bot R: x=-960, y=1260

page 2 top L: x=-960, y=504
page 2 bot R: x=-438, y=1260

button: x=-28, y=911

tab: x=-1639, y=362

docs: x=-831, y=1327

image: x=-1177, y=779

apply: x=-85, y=612

cantook: x=-1806, y=354

page w: 726
page h: 1052
'''