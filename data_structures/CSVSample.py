import csv
from time import sleep
from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By


# https://the-internet.herokuapp.com/login
driver = webdriver.Chrome()
with open("login.csv",'r') as csvfile:
    reader = csv.DictReader(csvfile) #Here my csv file is read as a dictionary
    print(reader.fieldnames)

    for row in reader:
        username = row['username']
        password = row['password']
        print(reader.line_num)
        print(username)
        print(password)
        driver.get("https://the-internet.herokuapp.com/login")
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button").click()
        sleep(5)
