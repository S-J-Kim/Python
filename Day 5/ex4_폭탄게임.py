num_of_players = int(input("게임 인원 입력 : "))
players = list(range(10))

start_player = int(input("몇번 플레이어 부터 시작합니까? : ")) - 1
step = int(input("폭탄 간격을 지정하세요 : "))

while len(players) > 1:
    print(f'{players[(start_player + step)%(len(players))] + 1}번 플레이어 아웃!')
    players.pop((start_player + step) % len(players))
    start_player = start_player + step - 2
    
print(f'{players[0]+1}번 플레이어 승리!')

    
