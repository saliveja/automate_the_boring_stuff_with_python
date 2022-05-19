import requests, sys, webbrowser, bs4

# open all the search results
print('Searching...')
res = requests.get('https://google.com/search?q=' 
                   'https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
# user will specify search terms using command line
# arguments will be stored as strings in a list in sys.argv
res.raise_for_status()