#The current sample data will be processed in this currentSample.py script
#By default, all samples will now automatically create and save an XLSX file for future processing. This is
#done by the saveToExcel() function.
import sys
sys.path.append("./openpyxl")
sys.path.append("./jdcal")
sys.path.append("./et_xmlfile")

import openpyxl


def saveToExcel():
	print('Current sameple signal information has been saved to Excel')

wb = openpyxl.load_workbook('Workbook1.xlsx')
print(type(wb))