
'''
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
# 10만원권, 5만원권, 1만원권, 5000원권, 1000원권, 500원권, 100원권
'''

#거스름돈 계산기 심자영
money = int(input("투입한 돈 얼마: "))
price = int(input("물건 값 얼마: "))

change = money - price
a = change // 100000
b = (change - (a * 100000)) // 10000
c = (change - (a * 100000) - (b * 10000)) // 5000
d = (change - (a * 100000) - (b * 10000) - (c * 5000)) // 1000
e = (change - (a * 100000) - (b * 10000) - (c * 5000) - (d * 1000)) // 500
f = (change - (a * 100000) - (b * 10000) - (c * 5000) - (d * 1000) - (e * 500)) // 100
     
print("거스름돈 : ", change)
print("10만원수표 : ", a,"개")
print("만원지폐 : ", b,"개") 
print("오천원지폐 : ", c,"개") 
print("천원짜리 : ", d,"개")
print("500원짜리 : ", e,"개") 
print("100원짜리 : ", f,"개") 

str(input("완료"))

#소스감사합니다.

