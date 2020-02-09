# 판다스에서 데이터처리 : 시리즈, 데이터프레임
# Series는 1차원 배열을 처리하고,
# DataFrame은 다차원배열을 처리한다.

import pandas as pd
import sys
import glob
import os

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []

for input_file in all_files :
        data_frame = pd.read_csv(input_file, index_col=None)
        
        total_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) \
  for value in data_frame.loc[:, 'Sale Amount']]).sum()

        average_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) \
  for value in data_frame.loc[:, 'Sale Amount']]).mean()

        data = {'file_name': os.path.basename(input_file),
                'total_sales': total_sales,
                'average_sales': average_sales}

        all_data_frames.append(pd.DataFrame(data, columns=['file_name','total_sales',\
                                                           'average_sales']))

data_frames_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frames_concat.to_csv(output_file, index=False)











        
                








        














        







