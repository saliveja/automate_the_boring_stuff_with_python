import requests

res = requests.get("https://automatetheboringstuff.com/files.rj.txt")
# pulling the text from the web page
type(res)
# checking what type of request
res.status_code == requests.codes.ok
# checking if the download went well
len(res.text)
# the number of characters in the text
print(res.text[:250])
# printing the first 250 characters
