import sys

print("Output : Baby_Shark.txt")

input_file = sys.argv[1]  # sys.argv[0] 은 현재 파일 자체를 의미함
filereader = open(input_file, 'r')

'''
r, w, a --> ASCII 모드에서 사용
rb, wb, ab --> binary 모드에서 사용
'''

for row in filereader:
    print(row.strip())

filereader.close()
