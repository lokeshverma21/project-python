# myapp/management/commands/run_selenium.py
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Command(BaseCommand):
    help = 'Run Selenium script'

    def handle(self, *args, **kwargs):
        # Initialize the WebDriver
        driver = webdriver.Chrome()  # or webdriver.Firefox() if you're using Firefox
        driver.get("http://chrome.com")  # Replace with your desired URL

        # Example interaction with the page
        search_box = driver.find_element("name", "q")
        search_box.send_keys("Selenium")
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)  # Let the user actually see something!

        # Print the title of the page
        self.stdout.write(driver.title)

        # Close the browser window
        driver.quit()
