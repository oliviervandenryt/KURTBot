from selenium import webdriver
from functions import *
from datetime import date, timedelta


''' PARAMETERS '''
username = "r0******"
password = "********"
times = [["08:00:00", "12:00:00"],  # tijdsloten van 4u
         ["12:00:00", "16:00:00"],
         ["16:00:00", "20:00:00"]
         ]
seat = str(100935) # zie .csv bestanden
date = str(date.today() + timedelta(days=1)) # bv. '2020-12-30'
subject = "Study"


'''CODE'''
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.switch_to.window(driver.current_window_handle)
login(driver, username, password)

for time in times:
    reserve(driver, date, time, seat, subject)
driver.close()
