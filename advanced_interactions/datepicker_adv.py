import time
import unittest


from selenium import webdriver

from selenium.webdriver.common.by import By


class TestDate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_date(self):
        self.driver.get("https://jqueryui.com/datepicker/#inline")
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading, "Datepicker")

        # 1. Find the frame webelement
        frame_element = self.driver.find_element(by=By.XPATH, value="//iframe[@class='demo-frame']")
        # 2. Switch to frame webelement
        self.driver.switch_to.frame(frame_element)
        time.sleep(1)

        # 3. Do element actions/processing - Click on element
        # Date, Month, Year
        sample_date = "1 November 2024"
        dt = sample_date.split(" ")[0]
        month = sample_date.split(" ")[1]
        year = sample_date.split(" ")[2]
        print(f'{dt} \t {month} \t {year}')

        curr_year = self.driver.find_element(by=By.XPATH, value="//span[@class='ui-datepicker-year']").text
        if curr_year == year:
            print('Correct Year')
        else:
            # Select correct year
            print('Code for correct year')

        curr_month = self.driver.find_element(by=By.XPATH, value="//span[@class='ui-datepicker-month']").text
        if curr_month == month:
            print('Correct Month')
        else:
            self.driver.find_element(by=By.XPATH, value="//span[text()='Prev']").click()
            # Select correct month

        dt_xpath = "//a[@data-date='" + dt + "']"
        self.driver.find_element(by=By.XPATH,value=dt_xpath).click()

        time.sleep(2)

        # 4. Switch back to default content
        self.driver.switch_to.default_content()
        time.sleep(1)
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading, "Datepicker")

    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
