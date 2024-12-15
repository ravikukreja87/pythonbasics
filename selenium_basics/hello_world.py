from selenium import webdriver
from selenium.webdriver.common.by import By

#Test automation script to perform google search

driver = webdriver.Chrome() #Launch Chrome browser
driver.get("https://www.google.com/") #Open the website

#I want to enter a text in google home page search box
#How I am doing this manually?
#1. I am looking for the text box where I have to enter the search term
#2. In selenium, looking for this field is locating/finding this field (web element)
#3. To explore all elements on the given page, we have developer tools in all browsers
#4. Identify element where we have to enter our search text in HTML DOM (Elements tab of developer tool)
#5. Identify tag name and various attributes

search_element = driver.find_element(by=By.NAME, value="q") #Located element
search_element.send_keys("Test string in google browser")
search_element.submit()
# search_button = driver.find_element(by=By.NAME, value="btnK")
# search_button.click()
print(driver.title)
#Assert - Compare actual and expected results.

# driver.find_element(by=By.NAME, value="my-text")
