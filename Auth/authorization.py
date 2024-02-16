import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Authorization:

    def __init__(self, driver: WebDriver, ):
        super().__init__()
        self.driver = driver

    def locate_email_field(self):
        email_field = self.driver.find_element(By.CLASS_NAME, "_aa4b._add6._ac4d._ap35")
        email_field.send_keys(Keys.CONTROL, 'v')

    def locate_name_field(self):
        name_field = self.driver.find_elements(By.CLASS_NAME, "_aa4b._add6._ac4d._ap35")
        if len(name_field) >= 2:
            name_field = name_field[1]
            name_field.send_keys("John")

    def locate_last_name_field(self):
        lastname_field = self.driver.find_elements(By.CLASS_NAME, "_aa4b._add6._ac4d._ap35")
        if len(lastname_field) >= 3:
            lastname_field = lastname_field[2]
            lastname_field.send_keys("Jackson12amid")

    def locate_password_field(self):
        password_field = self.driver.find_elements(By.CLASS_NAME, "_aa4b._add6._ac4d._ap35")
        if len(password_field) >= 4:
            password_field = password_field[3]
            password_field.send_keys("qwe123Q!")

    def insta_register_button(self):
        register_button = self.driver.find_elements(By.CLASS_NAME, "x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1xmf6yo.x1e56ztr.x540dpk.x1m39q7l.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1")
        if len(register_button) >= 2:
            register_button = register_button[1]
            register_button.click()
            time.sleep(10)

    def click_year_field(self):
        year_element = self.driver.find_element(By.CSS_SELECTOR, 'option[title="2001"][value="2001"]')
        year_element.click()
        time.sleep(2)

    def next_button(self):
        next_button = self.driver.find_element(By.CLASS_NAME, '_acan._acap._acaq._acas._aj1-._ap30')
        next_button.click()
        time.sleep(2)
