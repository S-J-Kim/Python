# 입력파일에서 특정 행을 필터링하는 세가지 방법
# 첫번째 : 특정 조건을 충족하는 행 필터링  --> 3번
# 두번째 : 특정 집합의 값을 포함하는 행을 필터링  --> 4번
# 세번째 : 정규표현식을 활용해 필터링  --> 5번


import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
                                                 .str.contains('Z')) | \
(data_frame['Cost'] > 600.0), :]

data_frame_value_meets_condition.to_csv(output_file, index=False)












				
