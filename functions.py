import csv
from time import sleep


def login(driver, username: str, password: str, given_sleep: float = 3.0):
    driver.get("https://bib.kuleuven.be/faciliteiten/reserveren")
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
    assert "Lokalen" in driver.title
    sleep(given_sleep / 15.0)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div[5]/div/div[1]/div[2]/p/a").click()
    sleep(given_sleep / 15.0)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("pwdLoginBtn").click()


def get_session_id(driver):
    driver.get(r"https://www-sso.groupware.kuleuven.be/sites/KURT/_vti_bin/KURTService/KURTService.svc/CallWebservice"
               r"?webserviceUrl=/GetSessionID")
    session_id = driver.find_element_by_xpath("/html/body/pre").text
    return session_id[3:-3]


def reserve(driver, date, time, seat, session_id, subject="Study", given_sleep: float = 3.0):
    url = f"https://www-sso.groupware.kuleuven.be/sites/KURT/Pages/NEW-Reservation.aspx?StartDateTime=" \
          f"{date}T{time[0]}&EndDateTime={date}T{time[1]}&ID={seat}&type=b&sessionId={session_id}"
    # multiline string
    print(url)
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.find_element_by_xpath('//*[@id="kurtResourceSubject"]').send_keys(subject)
    checkbox = driver.find_element_by_xpath('//*[@id="complyConditionsCheckbox"]')
    driver.execute_script("arguments[0].click();", checkbox)
    reservation_button = driver.find_element_by_id("submitReservationButton")
    driver.execute_script("arguments[0].click();", reservation_button)
    sleep(given_sleep * 0.66)


def get_name(driver, date, time, seat):
    url = f"https://www-sso.groupware.kuleuven.be/sites/KURT/Pages/NEW-Reservation.aspx?StartDateTime=" \
          f"{date}T{time[0]}&EndDateTime={date}T{time[1]}&ID={seat}&type=b"  # multiline string
    print(url)
    driver.get(url)
    sleep(0.9)
    display_name_text = driver.find_element_by_xpath('//*[@id="kurtResourceDisplayName"]').get_attribute('innerText')
    return str(display_name_text)


def update_csv(file, dictionary):
    with open(file, 'w') as f:
        w = csv.DictWriter(f, dictionary.keys())
        w.writeheader()
        w.writerow(dictionary)


def scrape(driver, begin, end, step, filename):
    labels = dict()
    for number in range(begin, end, step):
        a = get_name(driver, '2020-12-29', ["08:00:00", "12:00:00"], str(number))  # seats, times and date don't matter
        if a != '':
            labels[str(number)] = a
            print(a)
    update_csv(filename + '.csv', labels)
