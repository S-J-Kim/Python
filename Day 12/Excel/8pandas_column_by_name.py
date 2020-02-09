#파일명: 8pandas_column_by_name.py

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2017', index_col=None)

data_frame_column_by_name = data_frame.loc[:, ['Customer ID', 'Purchase Date']]

writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name='jan_17_output', index=False)
writer.save()
