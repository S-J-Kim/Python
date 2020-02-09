#파일명 : 5pan_value_in_set.py
#특정 집합을 충족하는 행의 필터링 => 기간이 2018/1/14 ~ 2018/1/31

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2017', index_col=None)
important_dates = ['01/16/2017', '01/31/2017']

data_frame_value_in_set = data_frame[data_frame['Purchase Date'].\
                                     isin(important_dates)]                                 
writer = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer, sheet_name='new_2017', index=False)
writer.save()







