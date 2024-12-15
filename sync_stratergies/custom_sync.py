import time
import unittest
from datetime import datetime

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class TestCustomWaits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_custom_wait(self):
        self.driver.get("https://agileway.com.au/demo/netbank")
        self.driver.find_element(by=By.ID, value="rcptAmount").send_keys("1000")
        account_drop_down = self.driver.find_element(by=By.NAME, value="account")
        Select(account_drop_down).select_by_visible_text("Savings")
        self.driver.find_element(by=By.ID, value="transfer_btn").click()

        timeout = 10
        start_time = datetime.now()


        while (datetime.now() - start_time).seconds < timeout:
            # (datetime.now() - start_time).seconds --> how many seconds have elapsed while I am retrying
            try:
                receipt_number = self.driver.find_element(by=By.ID, value="receiptNo").text
                receipt_date = self.driver.find_element(by=By.ID, value="date").text
                print(f'Receipt Number : {receipt_number}\nReceipt Date : {receipt_date}')
                break
            except NoSuchElementException:
                # retry until 10 seconds
                time.sleep(1)



    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
