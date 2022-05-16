import requests, bs4

res = requests.get("https://nostarch.com")
# downloads the main page from No Starch
res.raise_for_status()
# checking for errors
noStarchSoup = bs4.BeautifulSoup(examplefile, 'html.parser')
# parse = analysera. Processing information
type(exampleSoup)