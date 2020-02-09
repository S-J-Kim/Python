# 특정열을 선택하는 두가지방법
# 첫번째 열의 인덱스값을 사용하는 방법 - 6번
# 두번째 열의 헤더를 사용하는 방법 - 7번


import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

#my_columns = [0, 3]

data_frame = pd.read_csv(input_file)

data_frame_column_by_index = data_frame.iloc[:, [0, 3]]

data_frame_column_by_index.to_csv(output_file, index=False)







