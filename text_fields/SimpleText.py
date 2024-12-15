# Tag name of a field which accepts text from user in 'input'
# textarea

import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By


class TextSimple(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_text(self):
        self.driver.get("https://the-internet.herokuapp.com/inputs")
        # text_box = self.driver.find_element(by=By.XPATH,value="//input[@type='number']")
        text_box = self.driver.find_element(by=By.XPATH, value="//p[text()='Number']/following-sibling::input")
        text_box.send_keys("12345")
        time.sleep(2)

        self.driver.get("https://the-internet.herokuapp.com/key_presses")
        self.driver.find_element(by=By.ID, value="target").send_keys("This is a test str")
        time.sleep(5)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
