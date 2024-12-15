import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestNavigation(unittest.TestCase):
    base_url = "https://the-internet.herokuapp.com/"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_navigation(self):
        self.driver.get(self.base_url)

        self.visit_page("drag_and_drop", "//h3", "Drag and Drop")
        self.visit_page("checkboxes", "//h3", "Checkboxes")
        self.visit_page("dropdown", "//h3", "Dropdown List")

    def visit_page(self, path, xpath_str, expected_result):
        self.driver.get(self.base_url + path)
        self.driver.set_window_size(1024, 777)
        self.driver.set_window_position(100, 100)
        # time.sleep(2)
        self.query_heading_and_assert(xpath_str, expected_result)
        # time.sleep(2)
        self.driver.back()
        # time.sleep(2)
        self.driver.maximize_window()
        self.driver.set_window_position(0, 0)
        # Minimize window
        self.driver.set_window_position(-2000, 0)
        time.sleep(2)
        # self.driver.refresh()
        # time.sleep(2)

    def query_heading_and_assert(self, xpath_string, expected_result):
        heading = self.driver.find_element(by=By.XPATH, value=xpath_string).text
        print(heading)
        self.assertEqual(heading, expected_result)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()

# drag_and_drop
# checkboxes
# dropdown
