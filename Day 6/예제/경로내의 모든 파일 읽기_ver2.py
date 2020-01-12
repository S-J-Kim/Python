import sys
import glob  # 디렉토리 지정
import os  # 파일들을 합치는 역할

# Read multiple text files

input_path = sys.argv[1]
output_file=sys.argv[2]

# 인수로 받은 경로 내의 모든 텍스트파일을 읽어서 출력
for input_file in glob.glob(os.path.join(input_path, '*.txt')):
    print(os.path.basename(input_file))
    print('---------------------------------')
    with open(input_file, 'r', newline='', encoding="utf-8") as filereader:
        with open(output_file, 'a', newline='') as filewriter:
            for row in filereader:
                filewriter.write(row)
            filewriter.write("=============================\n")