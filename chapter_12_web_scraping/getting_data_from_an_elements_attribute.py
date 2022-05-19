import bs4

# getting data from an elements attribute
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
# using select to find a ny <span> elements
# storing in variable spanElem
print(str(spanElem))
# <span id="author">Al Sweigart</span>
print(spanElem.get('id'))
# returns author
print(spanElem.get('some_nonexistent_addr') == None)
# returns True
print(spanElem.attrs)
# {'id': 'author'}