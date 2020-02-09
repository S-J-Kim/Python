# 정규표현식 
import pandas as pd
import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

#pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number']\
                                                  .str.startswith('001-'), :]

data_frame_value_matches_pattern.to_csv(output_file, index=False)
