import time
from selenium import webdriver

# driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.get("https://agileway.com.au/demo")
# hardcoded wait (not a recommended way to wait)
time.sleep(5)
driver.quit()

# https://agileway.com.au/demo
