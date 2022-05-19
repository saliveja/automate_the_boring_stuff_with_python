import requests, bs4

res = requests.get("https://nostarch.com")
# downloads the main page from No Starch
res.raise_for_status()
# checking for errors
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# parse = analysera. Processing information
type(noStarchSoup)

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
# returns a list with all elements with id author
print(type(elems))
# returns <class 'list>
print(len(elems))
# number of items
print(type(elems[0]))
# what type index 0 is: <class 'bs4.element.Tag'>
print(str(elems[0]))
# returns string including tags and author
# <span id="author>Al Sweigart</span>
print(elems[0].getText())
# returns the name of the author
print(elems[0].attrs)
# returns the id tag
print("\n\n")

pElems = exampleSoup.select('p')
print(str(pElems[0]))
# returns the whole code of the paragraph: <p>Download my <strong>Python
# </strong> book from <a href="https://inventwithpython.com">my
# website</a>.</p>
print(pElems[0].getText())
# returns a readable text: Download my Python book from my website.
print(str(pElems[1]))
# <p class="slogan">Learn Python the easy way!</p>
print((pElems[1].getText()))
# Learn Python the easy way!
# getText() returns readable text without tags
print(str(pElems[2]))
print(pElems[2].getText())