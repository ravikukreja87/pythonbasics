from selenium import webdriver
from selenium.webdriver.common.by import By

# Test automation script to perform google search

driver = webdriver.Chrome()  # Launch Chrome browser
driver.get("https://www.google.com/")  # Open the website

search_element = driver.find_element(by=By.CLASS_NAME, value="gLFyf")  # Located element
search_element.send_keys("Test string in google browser")
search_element.submit()
print(driver.title)

# Strategies
# 1. By Name - Name attribute present in HTML DOM
# 2. By Id - Id attribute present in HTML DOM
# 3. By Tag_Name - TagName of Tag present in HTML DOM
# 4. By Class Name - Class attribute present in HTML DOM
# 5. By Link Text - Visible link text of Hyperlinks
# 6. By Partial Link Text - Substring of Visible link text of Hyperlinks
# Adv Strategies
# 7. CSS - CSS Selectors needs to be written which locate the element
# 8. XPATH - XPATH Strings needs to be written which locate the element


# Locators - String/Address to a WebElement. Unique address. Valid address.
# Locators Strategies - How to locate an element. How to use unique & valid address to locate an element.
# find_element(Strategy, Address/Locator String)

# find_address(Google Map, HouseNo, Area)
# find_address(Ask someone, Landmark)
# find_address(Past Knowledge, Address)
