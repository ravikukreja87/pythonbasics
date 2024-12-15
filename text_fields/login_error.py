# Tag name of a field which accepts text from user in 'input'
# textarea

import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By


class LoginSimple(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_login_error(self):
        self.driver.get("https://techedge.techcanvass.co/")
        self.login_steps("test", "test")
        self.handle_alert()
        self.login_steps("newuser", "test")
        self.handle_alert()

        # Exception is received here - StaleElementReferenceException
        # Solution is re-find the elements

    def login_steps(self, username, password):
        login_text_box = self.driver.find_element(by=By.NAME, value="txtLoginid")
        pass_text_box = self.driver.find_element(by=By.NAME, value="txtpassword")
        login_text_box.clear()
        pass_text_box.clear()
        login_text_box.send_keys(username)
        pass_text_box.send_keys(password)
        self.driver.find_element(by=By.NAME, value="btnLogin").click()
        time.sleep(2)

    def handle_alert(self):
        # Write code to check the alert message which is appearing on screen and press ok on the popup
        login_fail_alert = self.driver.switch_to.alert
        print(login_fail_alert.text)
        login_fail_alert.accept()
        # login_fail_alert.dismiss()
        time.sleep(2)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
