sec_input = int(input())  # 사용자에게 초단위 시간 입력

hour = sec_input // 3600  # 1시간은 3600초
minute = (sec_input % 3600) // 60 # 시간 단위로 나눈 나머지를 다시 분단위로 나눔
sec = (sec_input % 3600) % 60 # 초단위의 나머지 시간을 계산

print(f'{hour}시간 {minute}분 {sec}초')

