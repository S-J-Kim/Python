import sys
import glob  # 디렉토리 지정
import os  # 파일들을 합치는 역할

# Write to a text file

my_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

max_idx = len(my_letters)
output_file = sys.argv[1]  # 인자로 출력할 파일이름을 받는다
filewriter = open(output_file, 'w')


# my_letters 에서 한개씩 빼와서 출력한다. 
for idx_val in range(len(my_letters)):
    if idx_val < max_idx - 1:
        filewriter.write(my_letters[idx_val] + '\t')
    else:
        filewriter.write(my_letters[idx_val] + '\n')
    
filewriter.close()
print("Output : Output written to file")
