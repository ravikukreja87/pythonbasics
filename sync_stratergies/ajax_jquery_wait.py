import time
import unittest
from datetime import datetime

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class TestAJAXWaits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_ajax_wait(self):
        self.driver.get("https://travel.agileway.net/login")
        self.driver.find_element(by=By.ID, value="username").send_keys("agileway")
        self.driver.find_element(by=By.ID, value="password").send_keys("testwise")
        self.driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.ID, "flash_notice")))
        flash_notice = self.driver.find_element(by=By.ID, value="flash_notice").text
        print(f'{flash_notice} completed')

        self.driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()

        self.driver.find_element(by=By.NAME, value="passengerFirstName").send_keys("FirstName")
        self.driver.find_element(by=By.NAME, value="passengerLastName").send_keys("LastName")
        self.driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()

        self.driver.find_element(by=By.NAME, value="card_number").send_keys("1324")
        self.driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()

        self.wait_ajax(10)

        booking_number = self.driver.find_element(by=By.ID, value="booking_number").text
        print(f'Booking Number is {booking_number}')

    def wait_ajax(self, max_seconds):
        # jQuery.active
        count = 0
        while count < max_seconds:
            count += 1
            js = "return window.jQuery != undefined && jQuery.active == 0"
            is_ajax_complete = self.driver.execute_script(js)
            if is_ajax_complete:
                return
            else:
                time.sleep(1)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
