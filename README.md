# KURTBot
Automating KULeuven Reservation Tool. Uses a simple Selenium setup to be able to automate the process of booking a seat at the KULeuven libraries. To use effectively, setup a (free) AWS EC2 instance with a cron job for the script at 6PM GMT+2 each day.

## Installation
Make sure you have `selenium~=3.141.0` installed, and also add the Google Chrome webdriver to your PATH ([more info](https://chromedriver.chromium.org/getting-started))
## Usage
Parameters should be self explaining, for booking run `main.py`, for scraping/updating particular seat lists `scrape.py` can be used.
## Contributing
<a href="https://www.buymeacoffee.com/olivierv" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" > ></a>

Not needed, software should be fully functional. However this script is not guaranteed to be maintained and there is always room for improvement.  
  
**Last seat update**: *16/05/2021*  
**Last script update**: *21/05/2021*
