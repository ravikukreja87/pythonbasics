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

        # Use case 1 -->  3 Star and 2 Queen
        self.select_rating_bed_type("2 Queen", "3 Star")
        self.select_rating_bed_type("2 Queen", "3 Star") #Clean Up
        self.select_rating_bed_type("1 King", "5 Star")
        time.sleep(5)

    def select_rating_bed_type(self, which_bed_type, which_rating):
        time.sleep(1)
        hotel_ratings = self.driver.find_elements(by=By.XPATH,
                                                  value="//legend[text()='Hotel Ratings: ']/following-sibling::label")
        for hotel_rating in hotel_ratings:
            if which_rating in hotel_rating.text:
                hotel_rating.click()
        time.sleep(1)
        bed_types = self.driver.find_elements(by=By.XPATH,
                                              value="//legend[text()='Bed Type: ']/following-sibling::label")

        for bed_type in bed_types:
            if which_bed_type in bed_type.text:
                bed_type.click()

        time.sleep(1)


    def query_heading_and_assert(self, xpath_string, expected_result):
        heading = self.driver.find_element(by=By.XPATH, value=xpath_string).text
        print(heading)
        self.assertEqual(heading, expected_result)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
