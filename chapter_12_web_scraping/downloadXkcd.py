#! python3
# downloadXkcd.py

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
# making the folder xkcd
# or making an exception if the folder already exists

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

    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # download image
        print('Downloading image %s...' f'{comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        # 'wb' --> write binary

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print("Done.")
