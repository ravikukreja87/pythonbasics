import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestSlider(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_slider(self):
        self.driver.get("https://jqueryui.com/slider/#custom-handle")
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading, "Slider")

        # 1. Find the frame webelement
        frame_element = self.driver.find_element(by=By.XPATH, value="//iframe[@class='demo-frame']")
        # 2. Switch to frame webelement
        self.driver.switch_to.frame(frame_element)
        time.sleep(1)

        # 3. Do element actions/processing - Click on element
        slider = self.driver.find_element(by=By.ID, value="slider")

        ActionChains(self.driver).drag_and_drop_by_offset(slider,-20,0).perform()
        time.sleep(1)

        actual_text=self.driver.find_element(by=By.ID,value="custom-handle").text
        print(actual_text)

        # 4. Switch back to default content
        self.driver.switch_to.default_content()
        time.sleep(1)
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading, "Slider")

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
