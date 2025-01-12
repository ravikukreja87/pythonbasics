import csv
import os
import unittest
from datetime import datetime
from XTestRunner import HTMLTestRunner
import xlrd

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def navigate_to_login_page(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        heading = self.driver.find_element(by=By.XPATH, value="//h2").text
        print(heading)
        self.assertEqual(heading, "Login Page")

    def validate_flash_msg(self, expected_msg):
        actual_msg = self.driver.find_element(by=By.ID, value="flash").text
        self.assertTrue(actual_msg.__contains__(expected_msg))

    def test_login(self):
        print(os.path.dirname(os.path.realpath(__file__)))
        # Above stmt provides location of my current script/file
        # C:\Training2023\2024\PythonProjects\MyFirstPythonProject\MyFirstPythonProject\data_driven

        excel_file = os.path.dirname(os.path.realpath(__file__)) + "/test_data.xls"
        workbook = xlrd.open_workbook(excel_file)
        worksheet = workbook.sheet_by_name("data")
        num_rows = worksheet.nrows - 1
        curr_row = -1
        while curr_row < num_rows:
            curr_row += 1
            row = worksheet.row(curr_row)
            print(row)
            user_name = row[0].value
            user_password = row[1].value
            expected_result = row[2].value
            if user_name == "username":
                continue
            self.navigate_to_login_page()
            self.driver.find_element(by=By.ID, value="username").send_keys(user_name)
            self.driver.find_element(by=By.ID, value="password").send_keys(user_password)
            self.driver.find_element(by=By.XPATH, value="//button").click()
            self.validate_flash_msg(expected_result)
            self.custom_screenshot()

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()

    def custom_screenshot(self):
        screen_shot_file_name = str(datetime.now())
        screen_shot_file_name = screen_shot_file_name.split(".")[0]
        screen_shot_file_name = screen_shot_file_name.replace(":", "_")
        screen_shot_file_name = screen_shot_file_name.replace(" ", "_")
        print(screen_shot_file_name)
        self.driver.save_screenshot(screen_shot_file_name + "_login.png")


def Suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestAuth("test_login"))
    return suiteTest


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTests([
        TestAuth("test_login"),
    ])

    with(open('./result1.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='test report',
            description='describe: ... ',
            language='en',
            rerun=3
        )
        runner.run(suit)
