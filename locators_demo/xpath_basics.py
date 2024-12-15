import time
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By


class XpathBasics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_navigate_agile(self):
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")
        checkbox_one = self.driver.find_element(by=By.XPATH, value="//input[1]")
        checkbox_two = self.driver.find_element(by=By.XPATH, value="//input[2]")
        time.sleep(2)
        checkbox_one.click()
        time.sleep(2)
        checkbox_two.click()
        time.sleep(5)
    #     //input[1]

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()

# Seq - setUpClass --> setUp --> Each test --> tearDown --> tearDownClass
