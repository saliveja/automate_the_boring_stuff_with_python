import openpyxl
import os

wb = openpyxl.load_workbook('example.xlsx')
# returns value of workbook data type
print(type(wb))

dir = os.getcwd()
# returns the working directory
# we can use os.chdir() to change directory
print(dir)