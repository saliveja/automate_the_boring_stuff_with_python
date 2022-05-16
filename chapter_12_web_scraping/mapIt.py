#! python3
# mapIt.py

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    print(sys.argv)
    # the address that was written in the terminal
    # each word in this sentence will be part of a list
    # the first item on the list will be the name of the program
    address = '/' + ''.join(sys.argv[1:])
    address = '/' + ''.join(sys.argv[1:])
    # returns a single string from the lists
    # removes the name of the program
    # we start from index 1
# else:
#     address = pyperclip.paste()

webbrowser.open(f"https://www.google.com/maps/search{address}")