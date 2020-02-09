#파일명: 1csv.py
# 스크립트 파일과 작업파일이 다른 경우에 있을 경우 경로표기는 / 기호를 쓴다
# 만약, \ (백슬러시)기호를 사용할 경우 이스케이프 처리가 되므로 \\ 기호를 두개사용함.
# 파이썬에서 경로 표기할 경우 가급적이면 / 기호를 사용하는 것이 편리한다.


import sys

input_file = sys.argv[1]    # 읽어들일 파일을 지정한다
output_file = sys.argv[2]   # 저장할 파일이름 지정한다

# sys.argv[?] 사용할 경우 파일을 F5로 실행하기는 것이 아니고
# cmd에서 실행 ->   cmd> 스크립트파일명   읽을파일명   저장할파일명
#               예) cmd> 1csv.py  supplers.data_csv   ./NEW/1csv_out.csv


# r = read,  w = write,    a = append(마지막라인끝에 추가)
with open(input_file, 'r', newline='') as filereader :
    with open(output_file, 'w', newline='') as filewriter :
        header = filereader.readline() # 제목필드를 대상으로(한 줄만 읽는다)
        header = header.strip()   # 좌우 공백제거(엑셀:문자는우측정렬,숫자는좌측정렬)
        header_list = header.split(',')  # 콤마기호를 기준으로 필드(열)를 구분한다
        filewriter.write(','.join(map(str,header_list)) + '\n')
        for row in filereader :
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list)) + '\n')












        
        









