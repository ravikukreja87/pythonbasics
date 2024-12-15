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
        self.driver.find_element(by=By.XPATH,value="//button").click()
        self.driver.find_element(by=By.XPATH, value="//img[contains(@alt,'google')]").click()
        print(f'Google Playstore URL : {self.driver.current_url}')
        self.driver.back()
        self.driver.find_element(by=By.XPATH, value="//img[contains(@alt,'apple')]").click()
        print(f'Apple Store URL : {self.driver.current_url}')
        self.driver.back()
        print(f'Home Page URL : {self.driver.current_url}')
        time.sleep(2)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
