from datetime import date, timedelta

from functions import *

''' PARAMETERS '''
username = "r0******"
password = "****"
times = [["08:00:00", "10:00:00"],  # tijdsloten
         ["10:00:00", "13:00:00"],
         ["13:00:00", "19:00:00"],
         ["19:00:00", "22:00:00"]
         ]
seat = str(100804)  # zie .csv bestanden
date = str(date.today() + timedelta(days=3))  # bv. '2020-12-30'
subject = "Study"
default_sleep = 3.0  # bij problemen of traag internet verhogen

'''CODE'''
options = webdriver.ChromeOptions()
# options.add_argument('headless')

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.switch_to.window(driver.current_window_handle)
driver.maximize_window()

login(driver, username, password)

for time in times:
    reserve(driver, date, time, seat, subject)
driver.close()
