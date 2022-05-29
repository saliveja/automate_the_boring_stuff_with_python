from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests, bs4

browser = webdriver.Firefox()

#
browser.get('https://twitter.com/i/flow/login')
username_field = browser.find_element(By.CSS_SELECTOR, 'css-1dbjc4n r-18u37iz r-1pi2tsx r-1wtj0ep r-u8s1d r-13qz1uu')

username_field.send_keys('samuel.erixson@protonmail.com')
#
# next = browser.find_elements(By.CSS_SELECTOR, "css-901oao r-1awozwy "
#                                             "r-6koalj r-18u37iz r-16y2uox "
#                                             "r-37j5jr r-a023e6 r-b88u0q "
#                                             "r-1777fci r-rjixqe r-bcqeeo "
#                                             "r-q4m81j r-qvutc0")
#
# next.click()

# username = input('Username: ')
# password = input('Password: ')
#

#linkElem = browser.find_element(By.ID, 'rcmloginsubmit')
#
# username_field = browser.find_element(By.ID, 'rcmloginuser')
# username_field.send_keys("enchanted")
# #
# password_field = browser.find_element(By.ID, 'rcmloginpwd')
# password_field.send_keys("&P\{34KbY:Nd3V,2aJs^")
# #
# password_field.submit()
#
# time.sleep(3)
#
#
# compose = browser.find_element(By.ID, 'rcmbtn106')
# # if we choose 'elements' a list with objects is returned
# # list objects are not compatible with click() bcs they are multiple
# compose.click()
# print(compose)

# time.sleep(3)

# contact_button = browser.find_element(By.CLASS_NAME, 'input-group-append')
# contact_button.click()
#
# time.sleep(3)
#
# button_addresses = browser.find_element(By.ID, 'rcmliMA')
# button_addresses.click()
#
# time.sleep(3)
#
# selecting_contact = browser.find_element(By.ID, 'l:rcmrow0-20855046-0')
# selecting_contact.click()
#
# time.sleep(3)
#
# inserting_contact = browser.find_element(By.CLASS_NAME, 'mainaction insert recipient btn btn-primary')
# inserting_contact.click()
#
# time.sleep(3)

#
#
# #Setting the value of email input field
# driver.execute_script(f'var element = document.getElementById("email"); element.value = "{username}";')
#
# #Setting the value of password input field
# driver.execute_script(f'var element = document.getElementById("password"); element.value = "{password}";')
#
# #Submitting the form or click the login button also
# driver.execute_script(f'document.getElementsByClassName("login_form")[0].submit();')
#
# print(driver.page_source)



# res = requests.get("https://twitter.com/i/flow/login")
# # downloads the main page from No Starch
# res.raise_for_status()
# # checking for errors
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# # parse = analysera. Processing information
# type(noStarchSoup)
#
# elems = noStarchSoup.select('div')
# # returns a list with all elements with id author
# print(elems)
# # returns <class 'list>
# print(len(elems))
# # number of items
# print(type(elems[0]))
# # what type index 0 is: <class 'bs4.element.Tag'>
# print(str(elems[0]))
# # returns string including tags and author
# # <span id="author>Al Sweigart</span>
# print(elems[0].getText())
# # returns the name of the author
# print(elems[0].attrs)
# # returns the id tag
# print("\n\n")
#
# pElems = exampleSoup.select('p')
# print(str(pElems[0]))
# # returns the whole code of the paragraph: <p>Download my <strong>Python
# # </strong> book from <a href="https://inventwithpython.com">my
# # website</a>.</p>
# print(pElems[0].getText())
# # returns a readable text: Download my Python book from my website.
# print(str(pElems[1]))
# # <p class="slogan">Learn Python the easy way!</p>
# print((pElems[1].getText()))
# # Learn Python the easy way!
# # getText() returns readable text without tags
# print(str(pElems[2]))
# print(pElems[2].getText())