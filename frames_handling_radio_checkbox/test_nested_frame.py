import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNestedFrames(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_nested_frames(self):
        self.driver.get("https://the-internet.herokuapp.com/nested_frames")
        # Switch to frame using webelement
        # frame_element = self.driver.find_element(by=By.NAME, value="frame-bottom")
        # self.driver.switch_to.frame(frame_element)
        # Switch to frame using name attr
        self.driver.switch_to.frame("frame-bottom")
        actual_frame_text = self.driver.find_element(by=By.XPATH, value="//body").text
        expected_frame_text = "BOTTOM"
        print(f'Bottom Frame Text = {actual_frame_text}')
        self.assertEqual(actual_frame_text, expected_frame_text)
        self.driver.switch_to.default_content()

        self.switch_to_child_frame("frame-left","LEFT")
        self.switch_to_child_frame("frame-right", "RIGHT")
        self.switch_to_child_frame("frame-middle", "MIDDLE")

    def switch_to_child_frame(self,child_frame_name,expected_frame_text):
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame(child_frame_name)
        actual_frame_text = self.driver.find_element(by=By.XPATH, value="//body").text
        print(f'{expected_frame_text} Text = {actual_frame_text}')
        self.assertEqual(actual_frame_text, expected_frame_text)
        self.driver.switch_to.default_content()

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
