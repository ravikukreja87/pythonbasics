import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestHardcodedWaits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_hard_wait(self):
        self.driver.get("https://agileway.com.au/demo/netbank")
        self.driver.find_element(by=By.ID, value="rcptAmount").send_keys("1000")
        account_drop_down = self.driver.find_element(by=By.NAME, value="account")
        Select(account_drop_down).select_by_visible_text("Savings")
        self.driver.find_element(by=By.ID, value="transfer_btn").click()

        time.sleep(10)

        receipt_number = self.driver.find_element(by=By.ID, value="receiptNo").text
        receipt_date = self.driver.find_element(by=By.ID, value="date").text

        print(f'Receipt Number : {receipt_number}\nReceipt Date : {receipt_date}')

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
