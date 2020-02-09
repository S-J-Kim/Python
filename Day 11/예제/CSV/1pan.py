#파일명: 1pan.py

import sys
import pandas as pd


input_file = sys.argv[1]    # 읽어들일 파일을 지정한다
output_file = sys.argv[2]   # 저장할 파일이름 지정한다

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)


# pandas 모듈을 이용하면 더 간단하게 코드르 짤 수 있다.



        
        









