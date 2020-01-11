import random

end_seq = ''

print("주사위 게임 시작!")

while end_seq != 'q':
    print(random.randint(1, 6))
    end_seq = input("Enter는 한번 더, q는 종료 : ")
    