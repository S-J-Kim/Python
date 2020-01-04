#거스름돈 계산기 이 용규
money = int(input("투입한 돈 얼마: "))
price = int(input("물건 값 얼마: "))

change = money - price
x = change // 1000
y = (change - (x * 1000)) // 500
z = (change - (x * 1000) - (y * 500)) // 100

print("거스름돈 : ", change)
print("천원짜리 : ", x)
print("500원짜리 : ", y) 
print("100원짜리 : ", z) 

str(input("완료"))

# 8  / 4 # 몫과 나머지를 출력
# 8 // 4 # 몫만 출력
# 8  % 4 # 나머지만 출력