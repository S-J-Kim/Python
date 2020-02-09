import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, encoding='cp949')
writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='Bus_info', index=False, encoding='utf-8')
writer.save()
