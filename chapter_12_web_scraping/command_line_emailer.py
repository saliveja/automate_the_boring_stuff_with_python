from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://mail.riseup.net')

username = input('Username: ')
password = input('Password: ')

# linkElem = browser.find_element(By.ID, 'rcmloginsubmit')

username_field = browser.find_element(By.ID, 'rcmloginuser')
username_field.send_keys(username)

password_field = browser.find_element(By.ID, 'rcmloginpwd')
password_field.send_keys(password)

# password_field.submit()
browser.find_element(By.ID, 'rcmloginsubmit').submit()

compose = browser.find_element(By.ID, 'rcmbtn106')

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