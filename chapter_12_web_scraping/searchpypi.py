#! python3
# searchpypi.py
import requests, sys, webbrowser, bs4
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
}

# soup = BeautifulSoup(page, 'html.parser').find_all("a", class_="result__url", href=True)

if len(sys.argv) == 1:
    keyword = input('What to search> ')
else:
    keyword = sys.argv[1]
# open all the search results
print('Searching...')
# x = requests.get('https://w3schools.com')
res = requests.get('https://duckduckgo.com/?q=' + keyword, headers=headers)
# user will specify search terms using command line
# arguments will be stored as strings in a list in sys.argv
# join() takes one argument
res.raise_for_status()

# find all the results
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# processing the information in variable res
# print(soup)
linkElems = soup.select('#links')
# links are included i the class .package-snippet
# print(linkElems)

# open webbrowser for each result
numOpen = min(5, len(linkElems))
print("num", numOpen)
# by default the first five search results will open in new tabs
# or the number of links in the list linkElems -- whichever is smaller
# min() returns the smallest argument passed
for i in range(numOpen):
    urlToOpen = 'https://duckduckgo.com/?q=' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
print(res.status_code)