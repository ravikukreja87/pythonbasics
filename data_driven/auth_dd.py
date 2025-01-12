import csv
import os
import unittest
from datetime import datetime

import HtmlTestRunner

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

        csv_file = os.path.dirname(os.path.realpath(__file__)) + "/sample.csv"
        f = open(csv_file, 'rt')

        reader = csv.reader(f)
        for row in reader:
            # print(row)
            user_name = row[0]
            user_password = row[1]
            expected_result = row[2]
            if user_name == "username":
                continue
            self.navigate_to_login_page()
            self.driver.find_element(by=By.ID, value="username").send_keys(user_name)
            self.driver.find_element(by=By.ID, value="password").send_keys(user_password)
            self.driver.find_element(by=By.XPATH, value="//button").click()
            self.validate_flash_msg(expected_result)
            self.custom_screenshot()
        f.close()

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


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
