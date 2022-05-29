import openpyxl
import os

# opening excel docs with openpyxl
wb = openpyxl.load_workbook('example.xlsx')
# returns value of workbook data type
print(type(wb))

dir = os.getcwd()
# returns the working directory
# we can use os.chdir() to change directory
print(dir)

# getting sheets from the workbook
print(wb.sheetnames)
# ['Sheet1', 'Sheet2', 'Sheet3']

sheet = wb['Sheet3']
print(sheet)
# returns: <Worksheet "Sheet3">

print(type(sheet))
# returns: <class 'openpyxl.worksheet.worksheet.Worksheet'>

print(sheet.title)
# gets the title of the sheet

anotherSheet = wb.active
# getting the active sheet

print(anotherSheet)