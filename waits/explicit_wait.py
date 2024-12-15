import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class TestExplicitWaits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_explicit_wait(self):
        self.driver.get("https://agileway.com.au/demo/netbank")
        self.driver.find_element(by=By.ID, value="rcptAmount").send_keys("1000")
        account_drop_down = self.driver.find_element(by=By.NAME, value="account")
        Select(account_drop_down).select_by_visible_text("Savings")
        self.driver.find_element(by=By.ID, value="transfer_btn").click()

        wait = WebDriverWait(self.driver, 10)  # Initializing wait instance for driver
        # Max time is 10seconds
        # After 10 seconds script will timeout
        # Waiting until timeout or until a condition happens
        # What is the condition we are looking for in this use case?

        wait.until(expected_conditions.presence_of_element_located((By.ID, "receiptNo")))

        receipt_number = self.driver.find_element(by=By.ID, value="receiptNo").text
        receipt_date = self.driver.find_element(by=By.ID, value="date").text

        print(f'Receipt Number : {receipt_number}\nReceipt Date : {receipt_date}')

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
