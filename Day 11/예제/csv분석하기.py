import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# sys.argv[n] 사용할 경우 파일을 cmd에서 실행

with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        
        filewriter.write(','.join(map(str, header_list)) + '\n')

        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)

            filewriter.write(','.join(map(str, row_list)) + '\n')

        