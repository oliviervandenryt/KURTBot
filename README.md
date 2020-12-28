# KURTBot
Automating KULeuven Reservation Tool

# Info
Kan gebruikt worden vanaf 2 dagen op voorhand, uur maakt niet uit.
Bv. om 28 januari om 7u 's morgens is het al mogelijk om 30 januari de hele dag te reserveren.
Overmatig gebruik vermijden.

Voor mac gebruikers:
[_chromedriver_mac64.zip_](https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.27/) uitpakken in dezelfde map als main.py.

# Parameters:
Deze dienen allemaal aangepast te worden. De ID's voor Agora en CBA zijn te vinden in de csv bestanden.
```python
username = "r0******"
password = "********"
times = [["08:00:00", "12:00:00"],  # tijdsloten van 4u
         ["12:00:00", "16:00:00"],
         ["16:00:00", "20:00:00"]
         ]
seat = str(106602) # zie .csv bestanden
date = str(date.today() + timedelta(days=2)) # bv. '2020-12-30'
subject = "Study"
```
