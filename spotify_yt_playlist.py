import pyautogui
import time

count = 0

while True:
	pyautogui.click(x=375, y=245, clicks=1, button='right')
	pyautogui.click(x=406, y=438, clicks=1, button='left')
	time.sleep(0.5)
	pyautogui.click(x=824, y=558, clicks=3, button='left')
	pyautogui.hotkey('ctrl', 'c')
	pyautogui.click(x=1903, y=1039, clicks=1, button='left')
	pyautogui.press(['end', '[', '"'])
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press(['backspace', 'space', 'end', ',', 'space'])

	time.sleep(0.5)
	pyautogui.click(x=785, y=605, clicks=3, button='left')
	pyautogui.hotkey('ctrl', 'c')
	pyautogui.click(x=1903, y=1039, clicks=1, button='left')
	pyautogui.press(['end', 'left', 'left', 'left', 'left'])
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press(['backspace', 'end'])
	pyautogui.click(x=1136, y=487, clicks=1, button='left')
	time.sleep(0.5)
	pyautogui.scroll(-25)

	count =+ 1
	if count == 141:
		break

print('done')

'''
print(pyautogui.position())
'''