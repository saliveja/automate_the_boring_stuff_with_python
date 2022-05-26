from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://inventwithpython.com')
#
# try:
#     elem = driver.find_element(By.CLASS_NAME, 'container')
#     print('Found <%s> element with that class name!' % f'{elem.tag_name}')
#
# except:
#     print('Was not able to find and element with that name.')

linkElem = driver.find_element(By.LINK_TEXT, 'Read Online for Free')

print(type(linkElem))

linkElem.click()