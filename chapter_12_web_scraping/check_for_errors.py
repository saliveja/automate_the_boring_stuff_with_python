import requests

res = requests.get("https://inventwithpython.com/page_that_does_not_exist")
res.raise_for_status()
# stops the download if there is an error
# if it not a deal breaker, we can try except