# 숙제 2 : 숫자 야구게임 (4자리)
import random

def GenerateRandomNumber():
    num_list = [False for _ in range(10)]  # 숫자의 중복을 방지하기 위한 리스트
    num = []  # 생성된 숫자는 여기에 저장된다
    
    count = 4
    
    while count > 0:
        r = random.randint(0, 9)  # 임의의 한자리 숫자 생성

        if not num_list[r]:
            num.append(str(r))  # 생성된 숫자가 중복이 아니라면 리스트에 추가함
            num_list[r] = True  # 이 숫자는 이제 더 이상 생성되지 않는다
            count -= 1
    
    return num

def BallCount(generated_num, input_num):
    count = 0

    for i in range(4):  # 숫자는 같으나 자리는 다른 경우를 센다
        if input_num[i - 1] == generated_num[i] or input_num[i - 2] == generated_num[i] or input_num[i - 3] == generated_num[i]:
            count += 1

    return count

def StrikeCount(generated_num, input_num):
    count = 0

    for i, j in zip(generated_num, input_num):
        if i == j: count += 1  # 숫자와 자리가 모두 같은 경우를 센다

    return count

def BullsAndCows(generated_num):
    while True:
        user_input = list(input("숫자를 입력하세요 : "))

        balls = BallCount(generated_num, user_input)
        strikes = StrikeCount(generated_num, user_input)

        if strikes == 4:  # 4 스트라이크는 곧 모든 자리의 숫자가 서로 일치함을 의미함
            print("승리하였습니다!")
            break;
        
        elif strikes != 0 or balls != 0:
            print(f'{strikes}스트라이크 {balls}볼')

        else: print("아웃") # 스트라이크와 볼이 모두 0이면 아웃임


com_num = GenerateRandomNumber()  # 컴퓨터는 임의의 난수를 생셩함
BullsAndCows(com_num)
    
