import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestMultiSelect(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_multi_select(self):
        self.driver.get("https://jqueryui.com/selectable/")
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading, "Selectable")

        self.driver.find_element(by=By.LINK_TEXT,value="Display as grid").click()



        # 1. Find the frame webelement
        frame_element = self.driver.find_element(by=By.XPATH, value="//iframe[@class='demo-frame']")
        # 2. Switch to frame webelement
        self.driver.switch_to.frame(frame_element)
        time.sleep(1)

        # 3. Do element actions/processing - Click on element
        all_grid_items = self.driver.find_elements(by=By.XPATH,value="//ol/li")

        ActionChains(self.driver).click_and_hold(all_grid_items[1]).click_and_hold(all_grid_items[3]).click().perform()

        time.sleep(1)
        # 4. Switch back to default content
        self.driver.switch_to.default_content()
        time.sleep(1)
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading, "Selectable")

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
