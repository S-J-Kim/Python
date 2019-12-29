stadium = input("경기장은 어디입니까? : ")
winner = input("이긴팀은 어디입니까? : ")
loser = input("진 팀은 어디입니까? : ")
mvp = input("수훈선수는 누구입니까? : ")
score = input("스코어는 몇대몇입니까? : ")

prompt='''오늘 {}에서 야구 경기가 열렸습니다.
{}와 {}은 치열한 공방을 펼쳤습니다.
{}이 맹활약을 하였습니다.
결국 {}가 {}를 {}로 이겼습니다.''' \
    .format(stadium, winner, loser, mvp, winner, loser,score)
print("====================")
print(prompt)
print("====================")