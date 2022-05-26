from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

try:
    elem = driver.find_element(By.CLASS_NAME, ' .cover-thumb')
    print('Found <%s> element with that class name!' % f'{elem.tag_name}')
except:
    print('Was not able to find and element with that name.')