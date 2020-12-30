from selenium import webdriver
from functions import *
from datetime import date, timedelta


''' PARAMETERS '''
username = "r0******"
password = "********"
times = [["08:00:00", "12:00:00"],  # tijdsloten van 4u
         ["13:00:00", "17:00:00"],
         ["18:00:00", "22:00:00"]
         ]
seat = str(106602)  # zie .csv bestanden
date = str(date.today() + timedelta(days=2))  # bv. '2020-12-30'
subject = "Study"
default_sleep = 3.0  # bij problemen of traag internet verhogen


'''CODE'''
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.switch_to.window(driver.current_window_handle)
login(driver, username, password, sleep_time=default_sleep)

for time in times:
    reserve(driver, date, time, seat, subject, sleep_time=default_sleep)
driver.close()
