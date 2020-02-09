import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2017', index_col=None)
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.00]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='new_2017', index=False)
writer.save()