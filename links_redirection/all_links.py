import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By


class RedirectionDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_redirection(self):
        self.driver.get("https://techcanvass.com/")
        all_links_open_new_tab = self.driver.find_elements(by=By.XPATH, value="//a[contains(@target,'_blank')]")
        for each_link_ele in all_links_open_new_tab:
            each_link_text = each_link_ele.get_attribute("href")
            print(each_link_text)
        time.sleep(2)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
