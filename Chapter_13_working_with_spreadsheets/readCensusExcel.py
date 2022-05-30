#! python3
# readCensusExcel.py

import openpyxl, pprint
import os
import census2010

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}
# the dictionary will contain population and number of tracts for each county
# the key will be the state abbreviation

print('Reading rows...')
for row in range(2, sheet.max_row +1):
    # starting on two as the first is not containing the information we want
    # to the maximum number of rows
    # we want to cover all info
    # +1 to loop through the next tract each time and not the same
    state = sheet['B' + str(row)].value
    # B is the state abbreviation, row  read as strings,
    # pulling the value from the row
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    # making sure the key for the state exists
    # setting abbreviation as default and key
    # set default will do nothing if the key already exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    # making sure key for county in state exists and
    # setting default key and value to 0
    countyData[state][county]['tracts'] +=1
    # each row is one census tract
    # incrementing by one
    countyData[state][county]['pop'] += int(pop)
    # increasing county population by adding the population in the tract

print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('AllData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')

# census2010['AK']['Anchorage']
anchoragePop = census2010.AllData['AK']['Anchorage']['pop']
# All data is referring to the string in resultFile.write()
# it becomes the variable for the dictionary that will be written
# to census2010.py
print('The 2010 population of Anchorage was ' + str(anchoragePop))