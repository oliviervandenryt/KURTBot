from datetime import date, timedelta

from selenium import webdriver

from functions import *

from secrets import *
''' PARAMETERS '''
times = [["10:00:00", "13:00:00"],  # timeslots
         ["13:00:00", "19:00:00"],
         ["19:00:00", "22:00:00"],
         ["08:00:00", "10:00:00"]
         ]
date = str(date.today() + timedelta(days=4))  # bv. '2020-12-30'
subject = "Study"
default_sleep = 3.0  # increase when problems or slow internet

'''CODE'''
for index, username in enumerate(users):
    password = passwords[index]
    seat = seats[index]
    options = webdriver.ChromeOptions()
    # options.add_argument('headless') // remove commenting for running on a server
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(4)
    driver.switch_to.window(driver.current_window_handle)
    login(driver, username, password, default_sleep)
    for time in times:
        reserve(driver, date, time, seat, subject)
        sleep(1)
    driver.close()
