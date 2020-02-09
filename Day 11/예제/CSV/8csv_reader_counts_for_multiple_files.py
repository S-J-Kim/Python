#여러개의 파일을 통합작업하기
# sales_february_2019.csv, sales_january_2019.csv, sales_march_2019.csv

# 전채 파일 개수 및 각 파일의 행, 열의 숫자를 출력한다.


#!/usr/bin/env python3
import csv
import glob
import os
import sys

# CSV 파일들이 있는 폴더의 경로를 지정한다.
input_path = sys.argv[1]

file_counter = 0
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	row_counter = 1
	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		header = next(filereader)
		for row in filereader:
			row_counter += 1
	print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(\
	os.path.basename(input_file), row_counter, len(header)))
	file_counter += 1
print('Number of files: {0:d}'.format(file_counter))
