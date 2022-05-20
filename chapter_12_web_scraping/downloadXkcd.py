#! python3
# downloadXkcd.py

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
# making the folder xkcd
while not url.endswith('#'):
# the loop ends when the url ends with #
    print('Downloading page %s...' % url)
    # printing the url so we know which page we are downloading
    res = requests.get(url)
    # downloading url
    res.raise_for_status()
    # calling raise_the_status so that the download is stopped if
    # something went wrong

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # download page
    # find url
    # download image
    # save image to ./xkcd
    # get previous buttons url
print("Done.")