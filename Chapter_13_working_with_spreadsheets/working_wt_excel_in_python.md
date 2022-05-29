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
- x = sheet['nameOfCell].value						| returns the value in the cell. variable containing info of sheet + name of cell in []				|
- x.coordinate									| returns the name of the cell											|
- sheet.cell(row=1, column=2)							| Just like with the list, we can access a cell bu using cell()							|
- sheet.cell(row=1, column=2).value						| accessing the value of the cell											|
- sheet.max_row								| returning the highest row number											|
- sheet.max_column								| returning the highest column number											|
- get_column_letter(1)								| integers can be converted to letters with this									|
- column_index_from_string('A')						| string are converter to integers											|
- for rowOfCellObjects in sheet['A1':'C3']					| for loop with tuple focused on the rows in the specifies area							|
- for cellObj in rowOfCellObjects:						| for loop inside the first loop to access the cells in rowOfCells							|
- print(cellObj.coordinate, cellObj.value)					| returns the value of each cell in the specified area								|
- for cellObj in list(sheet.columns)[1]:					| refers to the value in index one for all rows									|
- print(cellObj.value)								| orint all cellObj values in index 1											|
- list(sheets.columns)[0]							| cell objects in column A												|
- list(sheets.columns)[1]							| cell objects in column B												|

