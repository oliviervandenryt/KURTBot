# KURTBot
Automating KULeuven Reservation Tool. Uses a simple Selenium setup to be able to automate the process of booking a seat at the KULeuven libraries. To use effectively, setup a (free) AWS EC2 instance with a cron job for the script at 6PM GMT+2 each day.

## Installation
Make sure you have `selenium~=3.141.0` installed, and also add the Google Chrome webdriver to your PATH ([more info](https://chromedriver.chromium.org/getting-started))
## Usage
Parameters should be self explaining, for booking run `main.py`, for scraping/updating particular seat lists `scrape.py` can be used.
## Contributing
Not needed, software should be fully functional. However this script is not guaranteed to be maintained and there is always remove for improvement.  
  
**Last seat update**: *16/05/2021*  
**Last script update**: *17/05/2021*
