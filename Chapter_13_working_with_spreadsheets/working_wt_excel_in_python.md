# Excel spread sheet

x		                       					|     															|
-----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------:|
openpyxl									| 															|
- variable = openpyxl.load_workbook('example.xlsx')				| returning info on workbook data type and give us access to info in the doc						|
- os.getcwd()									| returns the working directory											|
- os.chdir()									| changes working directory												|
- variable.sheetnames								| returns the names of the sheets in the doc										|
- sheet = variable['nameOfSheet']						| returns the worksheet object											|
- sheet.title									| gets the title of the sheet. to get the title we first have th call the item in the list.				|
- variable.active								| gets the active sheet												|
- type(sheet)									| returns what kind of sheet we are working with									|

   	
