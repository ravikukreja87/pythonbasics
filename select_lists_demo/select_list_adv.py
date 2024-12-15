import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestListsSelect(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_select(self):
        self.driver.get("https://jqueryui.com/selectmenu/#product-selection")
        self.driver.maximize_window()
        self.query_heading_and_assert("//h1", "Selectmenu")

        frame_element = self.driver.find_element(by=By.XPATH, value="//iframe[@class='demo-frame']")
        self.driver.switch_to.frame(frame_element)
        time.sleep(1)
        self.query_heading_and_assert("//label[text()='Circle radius']", "Circle radius")

        # 1. Find dropdown/locate drop down
        # select tag is my drop down

        # Use case --> Blue Circle with 200 px
        self.click_select_value("250px", "Black")
        time.sleep(5)
        # Adding assertion to check if circle is as per use case
        circle_specifications = self.driver.find_element(by=By.XPATH, value="//div[@id='circle']").get_attribute("style")
        print(circle_specifications)
        self.assertTrue(circle_specifications.__contains__("250px"))
        self.assertTrue(circle_specifications.__contains__("black"))

    def click_select_value(self, radius, color):
        self.driver.find_element(by=By.ID, value="radius-button").click()
        xpath_str = "//div[text()='" + radius + "']"
        self.driver.find_element(by=By.XPATH, value=xpath_str).click()
        self.driver.find_element(by=By.ID, value="color-button").click()
        xpath_str = "//div[text()='" + color + "']"
        self.driver.find_element(by=By.XPATH, value=xpath_str).click()

    def query_heading_and_assert(self, xpath_string, expected_result):
        heading = self.driver.find_element(by=By.XPATH, value=xpath_string).text
        print(heading)
        self.assertEqual(heading, expected_result)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
