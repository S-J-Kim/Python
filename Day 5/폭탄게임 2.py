# 폭탄돌리기 2

gamer_cnt = int(input("인원 결정 : "))
gamers = []

for x in range(gamer_cnt):
    gamers.append("user" + str(x + 1))

print(f'참가자 리스트 : {gamers}')

while True:
    start_point = int(input("시작 위치는 : "))
    
    if start_point > gamer_cnt:
        print("참가자 보다 큰 숫자는 지정할 수 없습니다.")
        pass

    pass_cnt = int(input("폭탄 간격지정 : "))
    idx_num = (start_point - 1 + pass_cnt) % gamer_cnt
    
    print(f'{gamers[idx_num]}은 아웃되었습니다.')
    
    gamers.pop(idx_num)
    gamer_cnt -= 1

    print(f'생존자 : {gamers}')

    if gamer_cnt == 1: print(f"게임을 종료합니다. 최종 승자는 {gamers[0]}입니다.")