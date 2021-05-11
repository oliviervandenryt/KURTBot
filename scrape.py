from selenium import webdriver

from functions import *

''' PARAMETERS '''
username = "r******"
password = "******"
start_id = 300000
end_id = 301000
step_size = 1
save_file = 'seat_lists/agora2'

'''CODE'''
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.switch_to.window(driver.current_window_handle)
login(driver, username, password)
scrape(driver, start_id, end_id, step_size, save_file)
driver.close()
