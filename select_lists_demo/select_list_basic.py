import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestListsSelect(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_select(self):
        self.driver.get("https://the-internet.herokuapp.com/dropdown")
        self.driver.maximize_window()
        self.query_heading_and_assert("//h3", "Dropdown List")

        drop_down = self.driver.find_element(by=By.ID,value="dropdown")

        # Select(drop_down).select_by_visible_text("Option 1")
        # Select(drop_down).select_by_index(2)
        Select(drop_down).select_by_value("1")
        time.sleep(2)
        #Clear the selection/deselect as well
        # Select(drop_down).deselect_by_value("1")
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
