import requests

res = requests.get("https://inventwithpython.com/page_that_does_not_exist")
try:
    res.raise_for_status()
    # stops the download if there is an error
    # if it not a deal breaker, we can try except
    # we should use raise_for_status() after requests.get()
except Exception as exc:
    print("There was a problem: %s" % (exc))