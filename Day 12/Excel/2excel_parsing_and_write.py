#파일명: 2excel_parsing_and_write.py

#!/usr/bin/env python3     
import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]    #파일명: sales_2017.xlsx 
output_file = sys.argv[2]   #파일명: ./NEW/2output.xls

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2017_output')

with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2017')
	for row_index in range(worksheet.nrows):
		for column_index in range(worksheet.ncols):
			output_worksheet.write(row_index, column_index, \
                                               worksheet.cell_value(row_index, column_index))
output_workbook.save(output_file)
