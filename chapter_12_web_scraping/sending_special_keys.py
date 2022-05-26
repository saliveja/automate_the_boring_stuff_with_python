from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('https://nostarch.com')
htmlElem = browser.find_element(By.TAG_NAME, 'html')
htmlElem.send_keys(Keys.END)
# scrolls down to the end of the page

time.sleep(5)
# pauses for five seconds

htmlElem.send_keys(Keys.HOME)
# returns to home
browser.refresh()
browser.quit()