#제목: 거스름돈 환전하기
#file: chage.py
#by: Julia Sim
#변수 선언: pmoney - 투입한 돈 / cost - 물건값 / change - 거스름돈 / paper - 지폐 / bcoin - 500원짜리 동전 / scoin - 100원
#출력: 거스름돈 - 1000원짜리 매수, 500원 동전 개수, 100원 동전 개수

pmoney=int(input("투입한 돈은 얼마입니까?  "))
cost=int(input("물건값은 얼마입니까?  "))
change=pmoney-cost
print("거스름돈은 ", change, "입니다")

paper=change//1000

change=change%1000

bcoins=change//500
change=change%500


scoin=change//100

print("1000원 지폐: ", paper,"장")
print("500원: ", bcoins,"개")
print("100원: ", scoin,"개")
