import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By


class ButtonsDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_buttons(self):
        self.driver.get("https://agileway.com.au/demo/")
        self.driver.find_element(by=By.XPATH, value="//a[text()='NetBank']").click()
        self.driver.find_element(by=By.NAME, value="amount").send_keys("5000")
        self.driver.find_element(by=By.XPATH, value="//input[@value='Transfer']").click()
        time.sleep(10)
        receipt_number = self.driver.find_element(by=By.ID, value="receiptNo").text
        date_of_transfer = self.driver.find_element(by=By.ID, value="date").text
        print(f'Receipt Number = {receipt_number}\nDate = {date_of_transfer}')
        # send_email(receipt_number,date)
        time.sleep(2)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
