# questions

**Describe difference between the webbrowser, requests, bs4 and selenium**

- webbbrowser --> opens the web page
- requests --> downloads the information from the web page
- bs4 --> processing the information, but ignores JavaScript
- selenium --> connects with the web browser. is an automatization tool


***What type of object is returned by requests.get()? How can we access the downloaded content as a string value?**

- requests.get() returns a Response()
- We can access it by storing it in a variable

**What requests method checks that the download worked?**
- raise_for_status()

**How to get an HTTP status code of a requests response?**

variable.status_code == requests.codes.ok

**How to save a requests response to a file?**
- variable = open("Name.txt", 'wb') --> wb, write binary
- for chunk in requestsVariable.iter_content(100000):
- variable.write(chunk)
- variable.close()


**Keyboard shortcut to opening the browsers developer tools?**
Ctrl+Shift+I

**How can you view (in developer tools) the HTML of a specific element on a web page?**
- through tags, like class, id, link, img
 
**What is the CSS selector string that would find the element with an id attribute of main?**
- by using # --> soup.select('#main')


**What is the CSS selector string that would find the elements with a CSS class of highlight?**
- using seleniums webdriver
- linkElem = driver.find_elements(By.CLASS_NAME, 'highlight')

**What is the CSS selector string that would find all the <div> elements inside another <div> element?**
- soup.select('div div')


**What is the CSS selector string to find the <button> element with a value attribute set to favorite?**
browser.find_element(By.ID, 'favorite')



**Say you have a Beautiful Soup tag object stored in the variable spam for the element <div>Hello world!</div>.**
**How could you get a string 'Hello world! from the tag object?**
- spam = exampleSoup.select('div')
- spam.getText()

**How would you store all the attributes of a Beautiful Soup tag object in a variable named linkElem?**
- exampleFile = open('example.html')
- exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
- linkElem = exampleSoup.select('a')


**Running import selenium doesn't work. How do you properly import the selenium module?**
- from selenium import webdriver --> tha main module
- from selenium.webdriver.common.by import By --> used for finding elements
- from selenium.webdriver.common.keys import Keys --> used for automatizing login for example

**What is the difference between find_element* and find_elements* method?**

**What metod do Selenium's WebElement objects have for simulating mouse clicks and keyboard keys?**
- click()
- submit()
- send_keys()

- selenium.webdriver.common.keys module
- Keys.DOWN
- Keys.UP
- Keys.LEFT
- Keys.RIGHT
- Keys.ENTER
- Keys.RETURN
- Keys.HOME
- Keys.END
- Keys.PAGE_UP
- Keys.PAGE_DOWN
- Keys.ESCAPE
- Keys.BACK_SPACE
- Keys.DELETE
- Keys,F1, Keys.F2 etc
- Keys.TAB


**You could call send_keys(Keys.ENTER) on the submit button's WebElement object, but what is an easier way to submit a form with Selenium?**
- submit()

**How can you simulate clicking a browser's Forward, Back and Refresh buttons with Selenium?**
- browser.refresh()
- browser.back()
- browser.forward()
