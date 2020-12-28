from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


def login(driver, username: str, password: str):
    driver.get("https://bib.kuleuven.be/faciliteiten/reserveren")
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
    assert "Lokalen" in driver.title
    sleep(0.2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div[5]/div/div[1]/div[2]/p/a").click()
    sleep(0.2)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("pwdLoginBtn").click()


def reserve(driver, date, time, seat, subject="Study"):
    url = f"https://www-sso.groupware.kuleuven.be/sites/KURT/Pages/NEW-Reservation.aspx?StartDateTime={date}T{time[0]}&EndDateTime={date}T{time[1]}&ID={seat}&type=b"
    print(url)
    driver.get(url)
    driver.find_element_by_id("kurtResourceSubject").send_keys(subject)
    driver.find_element_by_id("complyConditionsCheckbox").click()
    driver.find_element_by_id("submitReservationButton").click()


def get_name(driver, date, time, seat):
    url = f"https://www-sso.groupware.kuleuven.be/sites/KURT/Pages/NEW-Reservation.aspx?StartDateTime={date}T{time[0]}&EndDateTime={date}T{time[1]}&ID={seat}&type=b"
    print(url)
    driver.get(url)
    sleep(0.8)
    thisobj = driver.find_element_by_xpath("//*[@id='kurtResourceDisplayName']").get_attribute('innerText')
    return str(thisobj)


def update_csv(file, dictionary):
    with open(file, 'w') as f:
        w = csv.DictWriter(f, dictionary.keys())
        w.writeheader()
        w.writerow(dictionary)
