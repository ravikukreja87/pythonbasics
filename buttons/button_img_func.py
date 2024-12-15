import time
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By


class ButtonsImages(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_buttons_img(self):
        self.driver.get("https://techedge.techcanvass.co/")
        self.driver.find_element(by=By.XPATH, value="//button").click()
        self.navigate_store_url_back("google")
        self.navigate_store_url_back("apple")
        print(f'Home Page URL : {self.driver.current_url}')
        time.sleep(2)

    def navigate_store_url_back(self, app_store_name):
        self.driver.find_element(by=By.XPATH, value="//img[contains(@alt,'" + app_store_name + "')]").click()
        print(f'{app_store_name} Playstore URL : {self.driver.current_url}')
        self.driver.back()

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
