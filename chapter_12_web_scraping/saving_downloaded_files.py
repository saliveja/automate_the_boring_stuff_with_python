import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res. raise_for_status()
playFile = open("RomeoAndJuliet.txt", 'wb')
# changing name to RomeoAndJuliet
for chunk in res.iter_content(100000):
    # chunk is bytes
    # the size is passed through iter_content()
    playFile.write(chunk)

playFile.close()