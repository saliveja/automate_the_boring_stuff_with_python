import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
print(sheet['A1'])
# returning the defined cell
# <Cell 'Sheet1'.A1>

print(sheet['A1'].value)
# getting the value from the cell
# 2015-04-05 13:34:02

c = sheet['B1']
print(c.value)
# getting the value of B1 - Apples

print(f"Cell {c.coordinate} is {c.value}")
# c.coordinated returns the cell B1
# c.values returns the value of B1 which is Apples
# printing message containing this information

print(sheet['C1'].value)
# printing the value of C1