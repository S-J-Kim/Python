import random

options = ['왼쪽', '중앙', '오른쪽']  # 사용자가 선택 가능한 킥의 방향

com_choice = random.choice(options)  # 컴퓨터는 무작위로 수비할 방향을 선택
user_choice = input("킥 위치 입력 (왼쪽, 중앙, 오른쪽): ")

if com_choice == user_choice or user_choice == '': print("노골")
else: print("골")
