import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestListsSelectMulti(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_select_multi(self):
        self.driver.get("https://demoqa.com/select-menu")
        self.driver.maximize_window()
        self.query_heading_and_assert("//h1", "Select Menu")

        drop_down = self.driver.find_element(by=By.ID, value="cars")

        self.driver.execute_script("window.scrollTo(0,350)")
        # 0 --> Horizontal Scroll, 250 --> Vertical (Height) scroll
        time.sleep(5)
        Select(drop_down).select_by_visible_text("Volvo")
        Select(drop_down).select_by_index(2)
        Select(drop_down).select_by_value("audi")
        time.sleep(2)
        self.driver.save_screenshot("select_screen_shot.png")
        # Clear the selection/deselect as well
        Select(drop_down).deselect_by_value("audi")
        Select(drop_down).deselect_by_index(2)
        time.sleep(2)

        self.driver.save_screenshot("deselect_screen_shot.png")

        # Scroll to the end of page
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)

    def query_heading_and_assert(self, xpath_string, expected_result):
        heading = self.driver.find_element(by=By.XPATH, value=xpath_string).text
        print(heading)
        self.assertEqual(heading, expected_result)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
