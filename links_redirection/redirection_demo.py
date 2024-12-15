import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By


class RedirectionDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_redirection(self):
        self.driver.get("https://techcanvass.com/")
        current_offers_ele = self.driver.find_element(by=By.XPATH, value="//a[contains(text(),'Current')]")
        link_of_current_offers_page = current_offers_ele.get_attribute("href")
        self.driver.get(link_of_current_offers_page)
        #When I am clicking current offers, website is redirecting to new tab. Or opening link in new tab
        #Selenium/driver instance cannot automatically switch context to new tab
        #1. We switch to new tab/window (Later)
        #2. We do everything on same tab/window
        expected_title = "Techcanvass Courses Offers | Current Discounts"

        actual_title = self.driver.title

        self.assertEqual(actual_title, expected_title, "Titles do not match")

        time.sleep(2)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
