import time
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By

class XpathBasicsMultiple(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_xpath_basics_multiple(self):
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")
        all_checkboxes = self.driver.find_elements(by=By.XPATH, value="//input")

        # all_checkboxes is a list of 2 checkboxes that are present on that page

        for each_checkbox in all_checkboxes:
            each_checkbox.click()

        time.sleep(2)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()