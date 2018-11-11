import sys
sys.path.append("./openpyxl")
sys.path.append("./jdcal")
sys.path.append("./et_xmlfile")

dummyData = []

import openpyxl
fileLocation = './Workbook1.xlsx'
def getDataFromExcel(fileLocation):
	wb = openpyxl.load_workbook(fileLocation)
	sheet = wb.get_sheet_by_name('Sheet1')
	countrydata = {}
	for row in range(2,sheet.Max_Row()):
		state = sheet['B' + str(row)].value
		county = sheet['C' + str(row)].value
		pop = sheet['D'+ str(row)].value


