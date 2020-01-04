'''
#제목: 거스름톤 환전
#file: change.py

변수선언
1. 투입한 돈 = money
2. 물건 값 = price
3. 거스름돈 = change
   change = 투입한 돈 - 물건값
    조건1. 투입한 돈<물건값
4. 1000원지폐 = paper1000s
5. 500원동전 = coin500s
6. 100원동전 = coin100s

출력
7. 거스름돈 출력
  7-1. 1000원지폐 매수
  7-2. 500원동전 개수
  7-3. 100원동전 개수
'''
  
money=int(input("투입한 돈?: "))
price=int(input("물건 값?:  "))
change=money-price

paper1000s = change // 1000
change = change % 1000

coin500s = change//500

change = change%500
coin100s = change//100


#출력
#변수는 문자처리 안한다


print("천원짜리는",paper1000s,"장")    
print("500원짜리는",coin500s, "장")
print("100원짜리는",coin100s,"장")
