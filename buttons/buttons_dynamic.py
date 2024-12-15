import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By


class ButtonsDynamic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_buttons_dynamic(self):
        self.driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        time.sleep(2)
        # 1. Count total buttons initially
        list_of_all_buttons = self.driver.find_elements(by=By.XPATH, value="//button")
        count_of_all_button_before_click = len(list_of_all_buttons)
        print(f'Count of all button before click = {count_of_all_button_before_click}')  # 1
        # Click Add Element button
        self.driver.find_element(by=By.XPATH, value="//button").click()
        time.sleep(2)

        # After Click
        list_of_all_buttons_after_click = self.driver.find_elements(by=By.XPATH, value="//button")
        count_of_all_button_after_click = len(list_of_all_buttons_after_click)
        print(f'Count of all button after click = {count_of_all_button_after_click}')  # 2

        time.sleep(2)
        # Click Delete Button
        self.driver.find_element(by=By.XPATH, value="//button[text()='Delete']").click()
        time.sleep(5)
        list_of_all_buttons_after_delete = self.driver.find_elements(by=By.XPATH, value="//button")
        count_of_all_button_after_delete = len(list_of_all_buttons_after_delete)
        print(f'Count of all button after delete = {count_of_all_button_after_delete}')  # 1

        self.assertEqual(count_of_all_button_before_click, count_of_all_button_after_delete, "Count is not equal")

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
