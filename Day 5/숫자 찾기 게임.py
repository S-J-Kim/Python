import random

random_number = random.randint(1, 100)
count = 0

user_input = ''

while True:
    user_input = input("1~100 사이의 숫자 입력 : ")
    
    if int(user_input) < random_number: print("UP"); count += 1
    elif int(user_input) > random_number: print("DOWN"); count += 1
    else: break

print(f'정답! 시도 횟수 : {count+1}')