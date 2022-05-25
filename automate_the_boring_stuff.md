# Automate the boring stuff

x		                       					|     															|
-----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------:|
modules for web scraping							| webbrowser, requests, bs4, selenium											|
- webbbrowser									| opems the web page													|
- requests									| downloads the information from the web page										|
- bs4										| processing the information, but ignores JavaScript									|
- selenium									| connects with the web browser. is an automatization tool								|
web pages on requests								| requests.readthedocs.org/												|
res = requests.get()								| downloading information from specifies source, ie. web page, or a file						|
variable = bs4.BeautifulSoup(res.text, 'html.parser')			| processing the info													|
raise_for_status()								| stops the download if there is an error and communicates the error message						|
with open filename:	(or open())						| opens a file for appending, reading and writing									|
write()									| writes the content to the file											|
writelines()									| writes items in a list to a file											|
close()									| closes the file													|
iter_content()									| returns chunks of the content. in the brackets we can specify the bytes						|
css selectors --> information and below examples:				| nostarch.com/automatestuff2/											|
- soup.select('div')								| all elements named <div>												|
- soup.select('#author')							| the element with an id attribute of author										|
- soup.select('.notice')							| all elements that use a css class attribute named notice								|
- soup.select('div span')							| all elements names <span> that are within an element cnamed <div>							|
- soup.select('div > span')							| all elements names <span> that are directly within an element named <div> with no element between			|
- soup.select('input[name]')							| all elements named <input> that have a name attribute with any value						|
- soup.select('input[type="button]')						| all elements names <input> that have an attribute named type with value button					|
lxml module									| is an html parser, but faster than html.parser									|
- type()									| returns class													|
- type(nameoflist[0])								| return the class of index 0												|
- str(nameoflist[0])								| returns string including tags and the selected part ie. author. <span id="author>Al Sweigart</span>		|
variable = feedparser.parse()							| parsing rss feed													|
variable.entries								| displaying the entries in a rss feed										|
datetime.today().strftime('%Y-%m-%d %H:%M:%S')				| 2021-01-26 16:50:03													|
CSS										| CSS describes how HTML elements are to be displayed on screen, paper, or in other media				|
RSS										| a standardized system for the distribution of content from an online publisher					|
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')		| beautiful soup module, processing information in file								|
elems = exampleSoup.select('p')						| returns a list of all paragraphs											|
elems[0].gettext()								| returns a readble text without tags											|
sys.argv									|  is a list in Python, which contains the command-line arguments passed to the script				|
min()										| returns the smallest argument passed										|
webbrowser.open(urlToOpen)							| webbrowser module opens the first five search results by default							|
selenium import webdriver							| this is what we need to write to be able to use this module							|
url.endswith('#')								| can ie. be used in a while loop as 'while not url.endswith() as condition						|
url.startswith()								| can be udes as a condition if something starts with what we defined						|
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	        
