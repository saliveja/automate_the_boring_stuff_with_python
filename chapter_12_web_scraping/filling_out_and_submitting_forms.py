from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://login.metafilter.com')
userElem = browser.find_element(By.ID, 'user_name')
userElem.send_keys('your_real_username_here')

passwordElem = browser.find_element(By.ID, 'user_pass')
passwordElem.send_keys('your_real_password_here')
passwordElem.submit()