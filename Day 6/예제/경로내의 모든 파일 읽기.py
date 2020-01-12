import sys
import glob  # 디렉토리 지정
import os  # 파일들을 합치는 역할

# Read multiple text files

input_path = 'C:\\Users\\Python\\Desktop\\py\\Day 5\예제'

# 인수로 받은 경로 내의 모든 텍스트파일을 읽어서 출력
for input_file in glob.glob(os.path.join(input_path, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print(row.strip())
        print("=============================")