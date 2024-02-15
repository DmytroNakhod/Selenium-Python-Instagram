import constants as const
from config import Config
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# from Auth.auth import Authorization
# from ContactUs.contactUs import ContactForm


# WebDrivers configuration using the local storage
# Class Authorization for processing E2E tests for the Auth module functionality

def execute_tasks(_):
    try:
        with Config() as bot:
            bot.land_first_page()
            bot.close()
            bot.quit()
            input("Press enter to finish")

    except TimeoutException as e:
        print(f"Error: Timeout Open Login Page: {e}")
