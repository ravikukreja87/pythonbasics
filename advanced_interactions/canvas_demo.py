import base64
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCanvas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Launch Chrome browser

    def test_canvas(self):
        self.driver.get("https://www.chartjs.org/docs/latest/samples/bar/floating.html")
        heading = self.driver.find_element(by=By.XPATH, value="//h1").text
        print(heading)
        self.assertEqual(heading, "Floating Bars")

        canvas_ele = self.driver.find_element(by=By.XPATH,value="//canvas")
        js_scrap_image = "return arguments[0].toDataURL('image/png').substring(21);"
        canvas_base64 = self.driver.execute_script(js_scrap_image, canvas_ele)
        canvas_img = base64.b64decode(canvas_base64)

        file_path = "canvas.png"
        f = open(file_path, "wb")
        f.write(canvas_img)
        f.close()


    def tearDown(self):  # This will be called after every test
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):  # Will be called only once when all tests of class get executed
        cls.driver.quit()
