# Automate the boring stuff
_________________________________________________________________________________________________________________________________________________________________________________________________
x		                       					|     															|
-----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------:|
modules for web scraping							| webbrowser, requests, bs4, selenium											|
web pages on requests								| requests.readthedocs.org/												|
requests.get()									| downloading information from specifies source, ie. web page, or a file						|
raise_for_status()								| stops the download if there is an error and communicates the error message						|
with open filename:	(or open())						| opens a file for appending, reading and writing									|
write()									| writes the content to the file											|
writelines()									| writes items in a list to a file											|
close()									| closes the file													|
iter_content()									| returns chunks of the content. in the brackets we can specify the bytes						|
html.parser									| processes the downloaded html information										|
css selectors --> information and below examples:				| nostarch.com/automatestuff2/											|
	soup.select('div')							| all elements named <div>												|
	soup.select('#author')							| the element with an id attribute of author										|
	soup.select('.notice')							| all elements that use a css class attribute named notice								|
	soup.select('div span')						| all elements names <span> that are within an element cnamed <div>							|
	soup.select('div > span')						| all elements names <span> that are directly within an element named <div> with no element between			|
	soup.select('input[name]')						| all elements named <input> that have a name attribute with any value						|
	soup.select('input[type="button]')					| all elements names <input> that have an attribute named type with value button					|
	
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	        
