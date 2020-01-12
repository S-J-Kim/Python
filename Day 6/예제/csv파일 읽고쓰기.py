import sys
import glob  # 디렉토리 지정
import os  # 파일들을 합치는 역할

# Write to a text file

my_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

max_idx = len(my_numbers)
output_file = sys.argv[1]  # 인자로 출력할 파일이름을 받는다
filewriter = open(output_file, 'a')


# my_letters 에서 한개씩 빼와서 출력한다. 
for idx_val in range(len(my_numbers)):
    if idx_val < max_idx - 1:
        filewriter.write(my_numbers[idx_val] + ',')
    else:
        filewriter.write(my_numbers[idx_val] + '\n')
    
filewriter.close()
print("Output : Output written to file")
