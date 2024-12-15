import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFrames(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_frames(self):
        self.driver.get("https://jqueryui.com/checkboxradio/#default")
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading,"Checkboxradio")

        # 1. Find the frame webelement
        frame_element = self.driver.find_element(by=By.XPATH, value="//iframe[@class='demo-frame']")
        # 2. Switch to frame webelement
        self.driver.switch_to.frame(frame_element)
        time.sleep(1)
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading,"Checkbox and radio button widgets")

        # 3. Do element actions/processing - Click on element
        self.driver.find_element(by=By.XPATH, value="//input[@id='radio-1']/preceding-sibling::label").click()
        time.sleep(1)
        # 4. Switch back to default content
        self.driver.switch_to.default_content()
        time.sleep(1)
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading, "Checkboxradio")

        # 5. Navigate to Radio Group Link which is on Main HTML content
        self.driver.find_element(by=By.XPATH, value="//a[text()='Radio Group']").click()

        self.driver.switch_to.frame(0)
        #Name , Index , WebElement (WebElement of a frame)
        # frame_element = self.driver.find_element(by=By.XPATH, value="//iframe[@class='demo-frame']")
        # self.driver.switch_to.frame(frame_element)
        # time.sleep(1)

        heading = self.driver.find_element(by=By.XPATH, value="//h2").text
        print(heading)
        self.assertEqual(heading, "Radio Group")
        time.sleep(5)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
