'''
get all data from timetable
put time + room in a tuple
get list of all the classrooms
separate sections by start time
import that into code
tkinter
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
#//*[@id="result-message"]/div[SUBJECT]/div[COURSE]/ul[SECTION]/li[NOT IMPORTANT]/div/table/tbody/tr/td[1 IS DAY, 2 IS TIME, 3 IS ROOM]

PATH = Service("C:\\Users\\robom\\Desktop\\pyscripts\\_CHROMEDRIVER\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://dawsoncollege.omnivox.ca/intr")

search = driver.find_element(By.ID, "Identifiant")
search.send_keys('2137911')

search = driver.find_element(By.ID, "Password")
search.send_keys('at468hdg2KJLIN7NBA')

search.send_keys(Keys.RETURN)

time.sleep(3)
timetable = driver.find_element(By.XPATH, '//*[@id="ctl00_partOffreServices_offreV2_ctl275"]/span')
timetable.click()

ttab = driver.window_handles[1]
driver.switch_to.window(ttab)

choose_day = driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div[1]/form/fieldset[2]/div[2]/ul/li[1]/div/button')
choose_day.click()

#FOR MONDAY
select = driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div[1]/form/fieldset[2]/div[2]/ul/li[1]/div/div/ul/li[1]')
select.click()
choose_day.click()

#FOR STARTING @ 8AM
choose_time = driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div[1]/form/fieldset[2]/div[2]/ul/li[2]/div/button')
choose_time.click()

times = driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div[1]/form/fieldset[2]/div[2]/ul/li[2]/div/div/ul/li[1]/a')
times.click()

search = driver.find_element(By.XPATH, '//*[@id="btn-search"]')
search.click()

time.sleep(5)
open_all = driver.find_element(By.XPATH, '//*[@id="result-message"]/div[1]/div/a[1]')
open_all.click()

time.sleep(4)

n2 = 1
n3 = 1

day = driver.find_element(By.XPATH, f'//*[@id="result-message"]/div[2]/div[{n2}]/ul[{n3}]/li[5]/div/table/tbody/tr/td[1]').text
time = driver.find_element(By.XPATH, f'//*[@id="result-message"]/div[2]/div[{n2}]/ul[{n3}]/li[5]/div/table/tbody/tr/td[2]').text
room = driver.find_element(By.XPATH, f'//*[@id="result-message"]/div[2]/div[{n2}]/ul[{n3}]/li[5]/div/table/tbody/tr/td[3]').text

_8to12 = []
_8to10 = []
_8to1130 = []
_8to9 = []

while True:
	try:
		if day == 'Monday':
			if time == '8:00 AM - 12:00 PM':
				_8to12.append(room)
				print('1')

			elif time == '8:00 AM - 10:00 AM':
				_8to10.append(room)
				print('2')

			elif time == '8:00 AM - 11:30 PM':
				_8to1130.append(room)
				print('3')

			elif time == '8:00 AM - 9:00 AM':
				_8to9.append(room)
				print('4')
	except:
		break

	n2 += 1

print(_8to12)
print(_8to10)
print(_8to1130)
print(_8to9)