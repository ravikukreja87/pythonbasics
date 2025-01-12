import time
import unittest
from typing import KeysView

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestAutoComplete(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_auto_complete  (self):
        self.driver.get("https://jqueryui.com/autocomplete/")
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading, "Autocomplete")

        # 1. Find the frame webelement
        frame_element = self.driver.find_element(by=By.XPATH, value="//iframe[@class='demo-frame']")
        # 2. Switch to frame webelement
        self.driver.switch_to.frame(frame_element)
        time.sleep(1)

        # 3. Do element actions/processing - Click on element
        tags = self.driver.find_element(by=By.ID, value="tags")
        tags.send_keys("test data")
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()
        time.sleep(2)

        ActionChains(self.driver).send_keys(Keys.DELETE).perform()
        time.sleep(2)

        # 4. Switch back to default content
        self.driver.switch_to.default_content()
        time.sleep(1)
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading, "Autocomplete")

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
