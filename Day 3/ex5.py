inserted_money = input('투입한 돈 : ')
inserted_money = int(inserted_money)

price_of_goods = input('물건 값 : ')
price_of_goods = int(price_of_goods)

charge = inserted_money - price_of_goods  # 거스름 돈 계산

print(f'거스름돈 : {charge}원')


ten_thou = charge // 10000 # 거스름돈 중 만원짜리 지폐의 갯수
charge -= ten_thou * 10000
five_thou = charge // 5000 # 거스름돈 중 오천원짜리 지폐의 갯수
charge -= five_thou * 5000
thou = charge // 1000 # 거스름돈 중 천원짜리 지폐의 갯수

print(f'만원 지폐 : {ten_thou}장')
print(f'오천원 지폐 : {five_thou}장')
print(f'천원 지페 : {thou}장')