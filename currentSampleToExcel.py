#The current sample data will be processed in this currentSample.py script
#By default, all samples will now automatically create and save an XLSX file for future processing. This is
#done by the saveToExcel() function.
import sys
sys.path.append("./openpyxl")
sys.path.append("./jdcal")
sys.path.append("./et_xmlfile")

import openpyxl


link = 'Workbook1.xlsx'

def getDataFromAutochem():
	#insert conde to get data from autochem, let this test data be autochemData
	dummyAutoChemData = [(1,2),(2,4),(3,5)]
	saveToExcel(dummyAutoChemData)


def saveToExcel(autochemData):
	print('Current sameple signal information has been saved to Excel')

def getDataFromExcel(link):
	wb = openpyxl.load_workbook(link)
	sheet = wb.get_sheet_by_name('Sheet1')
	print(sheet.cell(row=3,column=2).value)
	cellInRow = sheet['A1':'B3']
	for row in cellInRow:
		for cell in row:
			print([cell.coordinate,cell.value])



getDataFromAutochem()