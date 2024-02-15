import constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#from Auth.auth import Authorization
#from ContactUs.contactUs import ContactForm


# WebDrivers configuration using the local storage
# Class Authorization for processing E2E tests for the Auth module functionality
class Config(webdriver.Chrome):
    def __init__(self, driver_path=r"D:\Work\Tools & instruments\Selenium\driver\chromedriver_win32",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Config, self).__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.tempmail_url)
