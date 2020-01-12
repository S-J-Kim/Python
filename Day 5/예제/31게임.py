# 31게임

# 규칙 1 : 30을 먼저 외치면 승리
# 규칙 2 : 2인용으로 제작
# 규칙 3 : 한 사람이 최대 3개까지 입력할 수 있다
# 규칙 4 : 0을 입력하면 턴을 넘긴다

# 예외 : 사용한 숫자 입력 불가, 범위내의 숫자만 입력해야 함

print("베스킨 라빈스 31 게임 시작")

number = 1

while number < 31:
    while True:
        player1 = int(input("(0은 종료) 플레이어 1번 순서, 숫자 입력 : "))
        
        if player1 == 0: break
        if player1 != number:
            print("잘못 입력했습니다. 다시 입력.")
            continue

        number = player1 + 1
        
    for i in range(number, 32):
        print(i, end=' ')
    
    print()

    while True:
        player2 = int(input("(0은 종료) 플레이어 2번 순서, 숫자 입력 : "))
        
        if player2 == 0: break
        if player2 != number:
            print("잘못 입력했습니다. 다시 입력.")
            continue

        number = player2 + 1
        
    for i in range(number, 32):
        print(i, end=' ')
    
    print()

print("30을 외쳤습니다. 승리!")