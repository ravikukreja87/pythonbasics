import time
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_search(self):
        self.driver.get("https://www.google.com/")  # Open the website
        search_element = self.driver.find_element(by=By.NAME, value="q")  # Located element
        search_element.send_keys("Test string in google browser")
        search_element.submit()
        time.sleep(5)

    def test_navigate_agile(self):
        self.driver.get("https://agileway.com.au/demo")
        time.sleep(5)

    def tearDown(self): #This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls): #Will be called only once when all tests of class get executed
        cls.driver.quit()

#Seq - setUpClass --> setUp --> Each test --> tearDown --> tearDownClass