import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

# print(tuple(sheet['A1':'C3']))

for rowOfCellObjects in sheet['A1':'C3']:
    # sheet[] is a tuple
    # it contains all row and cells from A1 to C3
    # starting top left and end bottom right
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
        # this loops through every item in the tuples
        # dates in A, names of fruits in B and numbers in C
        # it returns all of these values for A1 to c3
    print('---END OF ROW---')

for cellObj in list(sheet.columns)[1]:
    # for the objects with index position 1
    print(cellObj.value)
    # printing value of each cell object