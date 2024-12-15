import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFrames(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_frames(self):
        self.driver.get("https://jqueryui.com/checkboxradio/#default")
        self.query_heading_and_assert("//h1", "Checkboxradio")

        frame_element = self.driver.find_element(by=By.XPATH, value="//iframe[@class='demo-frame']")
        self.driver.switch_to.frame(frame_element)
        self.query_heading_and_assert("//h1", "Checkbox and radio button widgets")

        self.driver.find_element(by=By.XPATH, value="//input[@id='radio-1']/preceding-sibling::label").click()
        self.driver.switch_to.default_content()
        self.query_heading_and_assert("//h1", "Checkboxradio")

        self.driver.find_element(by=By.XPATH, value="//a[text()='Radio Group']").click()
        self.driver.switch_to.frame(0)

        self.query_heading_and_assert("//h2", "Radio Group")
        time.sleep(2)

        list_of_cities = self.driver.find_elements(by=By.XPATH, value="//label")
        # Assert number of check boxes
        self.assertEqual(len(list_of_cities), 3)
        self.click_city(list_of_cities, "London")
        self.click_city(list_of_cities, "New York")
        self.click_city(list_of_cities, "Paris")

        # Use case, I only want to click Paris
        # Use case, I click London --> New York --> Paris

    def click_city(self, list_of_cities, city_to_click):
        for city in list_of_cities:
            if city_to_click in city.text:
                city.click()
                time.sleep(3)

    def query_heading_and_assert(self, xpath_string, expected_result):
        heading = self.driver.find_element(by=By.XPATH, value=xpath_string).text
        print(heading)
        self.assertEqual(heading, expected_result)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
