# Excel spread sheet

x		                       						|     															|
-------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------:|
openpyxl										| 															|
- variable = openpyxl.load_workbook('example.xlsx')					| returning info on workbook data type and give us access to info in the doc						|
- os.getcwd()										| returns the working directory											|
- os.chdir()										| changes working directory												|
- variable.sheetnames									| returns the names of the sheets in the doc										|
- sheet = variable['nameOfSheet']							| returns the worksheet object											|
- sheet.title										| gets the title of the sheet. to get the title we first have th call the item in the list.				|
- variable.active									| gets the active sheet												|
- type(sheet)										| returns what kind of sheet we are working with									|
- x = sheet['nameOfCell].value							| returns the value in the cell. variable containing info of sheet + name of cell in []				|
- x.coordinate										| returns the name of the cell											|
- sheet.cell(row=1, column=2)								| Just like with the list, we can access a cell bu using cell()							|
- sheet.cell(row=1, column=2).value							| accessing the value of the cell											|
- sheet.max_row									| returning the highest row number											|
- sheet.max_column									| returning the highest column number											|
- get_column_letter(1)									| integers can be converted to letters with this									|
- column_index_from_string('A')							| string are converter to integers											|
- for rowOfCellObjects in sheet['A1':'C3']						| for loop with tuple focused on the rows in the specifies area							|
- for cellObj in rowOfCellObjects:							| for loop inside the first loop to access the cells in rowOfCells							|
- print(cellObj.coordinate, cellObj.value)						| returns the value of each cell in the specified area								|
- for cellObj in list(sheet.columns)[1]:						| refers to the value in index one for all rows									|
- print(cellObj.value)									| orint all cellObj values in index 1											|
- list(sheets.columns)[0]								| cell objects in column A												|
- list(sheets.columns)[1]								| cell objects in column B												|
- youEmptyDictName.setdefault(nameOfKey, {})						| making sure key exists. If the key exist, nothing changes. If not, this value becomes the key's value		|
- youEmptyDictName[nameOfKey].setdefault(anotherKey, {'value1': 0, 'value2': 0})	| making sure the key exists and setting default values								|
- youEmptyDictName[nameOfKey][anotherKey]['value1'] +=1				| going through all the values, adding one value to another until toal count						|
- youEmptyDictName[nameOfKey][anotherKey]['value2'] += int(value2)			| as above but specifying that the increment is an integer								|
- resultFile = open('nameOfFile.py', 'w')						| we create a file where we can store the data									|
- resultFile.write('AllData = ' + pprint.pformat(youEmptyDictName))			| pprint formats the data so it can be used as input to the interpreter						|
- x = nameOfFile.AllData['valueRowA1']['valueRowA2']['keyA3']			| storing the data we want to see in a variable, example of sequence							|
- variable = openpyxl.Workbook()							| creates a new excel document											|
- variable.create_sheet()								| creates a new sheet in the excel document										|
- variable.create_sheet(index=0, title='New Name')					| creating a new sheet at a specific position with a specific name							|
- del variable['nameOfSheetToDel']							| deleting sheet													|
