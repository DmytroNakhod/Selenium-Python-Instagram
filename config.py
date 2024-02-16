import time
import constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Auth.authorization import Authorization


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
        self.tempmail_email_code = {}

    def open_new_tab(self, url):
        self.execute_script("window.open('{}', '_blank');".format(url))

    def switch_to_tab(self, tab_index):
        self.switch_to.window(self.window_handles[tab_index])

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_tempmail_page(self):
        self.get(const.tempmail_url)
        time.sleep(5)

    def get_element_copy_button(self):
        self.find_element(By.CLASS_NAME, "kopyala-link").click()

    def appy_registration(self):
        self.open_new_tab(const.instagram_url)  # Open to the new tab
        self.switch_to_tab(1)
        registration = Authorization(driver=self)
        registration.locate_email_field()
        registration.locate_name_field()
        registration.locate_last_name_field()
        registration.locate_password_field()
        registration.insta_register_button()
        registration.click_year_field()
        registration.next_button()
        print("Registration finished")
        self.switch_to_tab(0)
        time.sleep(2)

    def close_alert_popup(self):
        close_button = self.find_element(By.XPATH, '//svg[@fill="#5F6368"]')
        close_button.click()
        time.sleep(2)

    def click_on_email(self):
        try:
            element = WebDriverWait(self, 50).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="https://tempail.com/en/mail_"]'))
            )
            element.click()
        except TimeoutException:
            print("Timeout Exception")

    def copy_past_code_from_email(self):
        letter_info = webdriver.Chrome.find_element(By.CSS_SELECTOR, "div[dir='ltr']")
        text = letter_info.text
        self.tempmail_email_code['email_code'] = text
        self.switch_to_tab(1)
        time.sleep(2)

        input_element = self.find_element(By.XPATH, "input[aria-label='Код подтверждения']")
        verification_code = self.tempmail_email_code.get('email_code', '')
        input_element.send_keys(verification_code)
        next_button = self.find_element(By.XPATH, "div[@role='button']/[@tabindex='-1']")
        next_button.click()
