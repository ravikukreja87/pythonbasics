import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By


class LinkTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_link_get_info(self):
        self.driver.get("https://agileway.com.au/demo/survey")
        # Locate link as webelement first

        try:
            link_ele = self.driver.find_element(by=By.XPATH, value="//a")
            self.assertTrue(link_ele.is_displayed())
            href_attr_value = link_ele.get_attribute("href")
            # self.driver.get(href_attr_value)
            link_tag_name = link_ele.tag_name
            link_value = link_ele.text

            print(f'Link Tag Name : {link_tag_name}\nValue is : {link_value}\nHref Attr is : {href_attr_value}')

            expected_link_value = "Download TestWise Recorder"
            self.assertEqual(expected_link_value, link_value, "Do not match")

            link_ele.click()
        except NoSuchElementException:
            print('Link is not available')
        # all_checkboxes is a list of 2 checkboxes that are present on that page
        time.sleep(2)

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
