from selenium import webdriver

from functions import *

from secrets import *

''' PARAMETERS '''
username = users[0]
password = passwords[0]
start_id = 110001  # starting seat
end_id = 110140  # ending seat
step_size = 1  # step size in seat enumeration
save_file = 'seat_lists/fac'  # name & location for the csv

'''CODE'''
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.switch_to.window(driver.current_window_handle)
login(driver, username, password)
scrape(driver, start_id, end_id, step_size, save_file)
driver.close()
