from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://mail.com')

linkElem = browser.find_element(By.ID, 'login-button')
linkElem.click()

userElem = browser.find_element(By.ID, 'login-email')
userElem.send_keys('your_real_username_here')

passwordElem = browser.find_element(By.ID, 'login-password')
passwordElem.send_keys('your_real_password_here')
passwordElem.submit()