import csv
from time import sleep
from datetime import timedelta


def login(driver, username: str, password: str, given_sleep: float = 3.0):
    driver.get("https://kuleuven.be/kurt")
    sleep(given_sleep / 15.0)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("pwdLoginBtn").click()


def get_session_id(driver):
    driver.get(r"https://www-sso.groupware.kuleuven.be/sites/KURT/_vti_bin/KURTService/KURTService.svc/CallWebservice"
               r"?webserviceUrl=/GetSessionID")
    session_id = driver.find_element_by_xpath("/html/body/pre").text
    return session_id[3:-3]


def reserve(driver, user, date, time, sid, session):
    if time[1] == "00:00:00":
        date2 = str(date + timedelta(days=1))
        date = str(date)
        javascript = f"fetch('https://www-sso.groupware.kuleuven.be/sites/KURT/_vti_bin/KURTService/KURTService.svc" \
                     f"/CallWebservice?webserviceUrl=/CreateReservation4?CurrentUID={user}%26SelectedResourceID={sid}" \
                     f"%26SelectedBeginDatestring={date}%20{time[0]}%26SelectedEndDatestring={date2}%20{time[1]}" \
                     f"%26Subject=U3R1ZHk=%26Body=%26OtherUsers=%26Answer=%26ImpersonatedUID=%26SessionID={session}')"
    else:
        date = str(date)
        javascript = f"fetch('https://www-sso.groupware.kuleuven.be/sites/KURT/_vti_bin/KURTService/KURTService.svc" \
                     f"/CallWebservice?webserviceUrl=/CreateReservation4?CurrentUID={user}%26SelectedResourceID={sid}" \
                     f"%26SelectedBeginDatestring={date}%20{time[0]}%26SelectedEndDatestring={date}%20{time[1]}" \
                     f"%26Subject=U3R1ZHk=%26Body=%26OtherUsers=%26Answer=%26ImpersonatedUID=%26SessionID={session}')"
    driver.execute_script(javascript)
    print(f"Booking complete for: at {date} from {time[0]} to {time[1]}")


def get_name(driver, date, time, seat):
    date = str(date)
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
