import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, encoding='cp949')
print(data_frame)
data_frame.to_csv(output_file, index=False, encoding='utf-8')
