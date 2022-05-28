from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime

driver = webdriver.Firefox()
driver.get('https://twitter.com/i/lists/1345778435390640129')

while True:
    num = str(datetime.datetime.now())
    htmlElem = driver.find_element(By.TAG_NAME, 'html')
    htmlElem.send_keys(Keys.PAGE_DOWN)

    driver.save_screenshot(f'twitter{num}.png')
    if htmlElem == Keys.END:
        browser.quit()