import time
import unittest
from datetime import datetime
from typing import KeysView

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from locators_demo.xpath_basics import XpathBasics


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def navigate_to_login_page(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        heading = self.driver.find_element(by=By.XPATH, value="//h2").text
        print(heading)
        self.assertEqual(heading, "Login Page")

    def login(self, username, password):
        self.driver.find_element(by=By.ID, value="username").send_keys(username)
        self.driver.find_element(by=By.ID, value="password").send_keys(password)
        self.driver.find_element(by=By.XPATH, value="//button").click()

    def validate_flash_msg(self, expected_msg):
        actual_msg = self.driver.find_element(by=By.ID, value="flash").text
        self.assertTrue(actual_msg.__contains__(expected_msg))

    def test_login_success(self):
        self.navigate_to_login_page()
        self.login("tomsmith", "SuperSecretPassword!")
        self.validate_flash_msg("You logged into a secure area!")
        self.driver.find_element(by=By.XPATH,value="//a[@class='button secondary radius']").click() #Click logout
        self.validate_flash_msg("You logged out of the secure area!")

    def test_login_failure(self):
        self.navigate_to_login_page()
        self.login("tomsmith", "incorrect!")
        self.validate_flash_msg("Your password is invalid!")

    def test_login_failure_username(self):
        self.navigate_to_login_page()
        self.login("tmsmith", "incorrect!")
        self.validate_flash_msg("Your username is invalid!")

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)
        screen_shot_file_name = str(datetime.now())
        screen_shot_file_name = screen_shot_file_name.split(".")[0]
        screen_shot_file_name = screen_shot_file_name.replace(":","_")
        screen_shot_file_name = screen_shot_file_name.replace(" ", "_")
        print(screen_shot_file_name)
        self.driver.save_screenshot(screen_shot_file_name + "_login.png")

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
