#! python3
# searchpypi.py
import requests, sys, webbrowser, bs4

headers = {"User-Agent": "Mozilla/5.0"}

if len(sys.argv) == 1:
    keyword = input('What to search> ')
else:
    keyword = sys.argv[1]
# open all the search results
print('Searching...')
# x = requests.get('https://w3schools.com')
res = requests.get('https://google.com/search?q=' + keyword)
# user will specify search terms using command line
# arguments will be stored as strings in a list in sys.argv
# join() takes one argument
res.raise_for_status()

# find all the results
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# processing the information in variable res
print(soup)
linkElems = soup.select('.r a')
# links are included i the class .package-snippet
# print(linkElems)

# open webbrowser for each result
numOpen = min(5, len(linkElems))
print("num", numOpen)
# by default the first five search results will open in new tabs
# or the number of links in the list linkElems -- whichever is smaller
# min() returns the smallest argument passed
for i in range(numOpen):
    urlToOpen = 'https://google.com/' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
print(res.status_code)


#
#
# import requests, sys, webbrowser, bs4
#
# print('Googling...') # display text while downloading the Google page
# res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]), 'lxml')
# res.raise_for_status()
#
# # Retrieve top search result links.
# soup = bs4.BeautifulSoup(res.text, 'lxml')
#
# # Open a browser tab for each result.
# linkElems = soup.select('.r a')
# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     webbrowser.open('http://google.com' + linkElems[i].get('href'))