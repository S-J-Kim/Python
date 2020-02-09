# 특정 집합의 값을 만족하는 열의 필터링 : 기간을 만족

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

important_dates = ['1/20/19', '1/31/19']
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date']\
                                         .isin(important_dates), :]

data_frame_value_in_set.to_csv(output_file, index=False)
