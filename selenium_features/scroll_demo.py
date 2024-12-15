import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestScroll(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_scroll(self):
        self.driver.get("https://the-internet.herokuapp.com/infinite_scroll")
        self.driver.maximize_window()
        self.query_heading_and_assert("//h3", "Infinite Scroll")
        time.sleep(2)
        #Scroll down

        for i in range(1,10):
            self.driver.execute_script("window.scrollTo(0,250)")
            # 0 --> Horizontal Scroll, 250 --> Vertical (Height) scroll
            time.sleep(2)

    def query_heading_and_assert(self, xpath_string, expected_result):
        heading = self.driver.find_element(by=By.XPATH, value=xpath_string).text
        print(heading)
        self.assertEqual(heading, expected_result)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
