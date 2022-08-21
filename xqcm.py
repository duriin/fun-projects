from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import random

options = Options()
options.headless = True

PATH = 'G:\\Users\\cheng\\Desktop\\pystuff\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

count = 0

while True:
	driver.get('https://forms.gle/QPkDCRTTRZo47TF1A')

	nums1 = ['i5','i8','i11']
	for a in (random.choices(nums1, weights = [70,20,10], k = 1)):
		pass

	nums2 = ['i18','i21','i24']
	for b in (random.choices(nums2, weights = [70,20,10], k = 1)):
		pass

	driver.find_element_by_xpath(f'//*[@id="{a}"]/div[3]/div').click()

	driver.find_element_by_xpath(f'//*[@id="{b}"]/div[3]/div').click()

	driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div/span/span').click()

	count += 1
	print(count)
	if count == 88:
		break