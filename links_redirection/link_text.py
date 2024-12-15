import time
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By


class LinkTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_link(self):
        self.driver.get("https://agileway.com.au/demo/survey")
        # Locate link as webelement first

        try:
            link_ele = self.driver.find_element(by=By.XPATH, value="//a")
            self.assertTrue(link_ele.is_displayed())
            link_ele.click()
        except:
            print('Link is not available')
        # all_checkboxes is a list of 2 checkboxes that are present on that page
        time.sleep(2)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
