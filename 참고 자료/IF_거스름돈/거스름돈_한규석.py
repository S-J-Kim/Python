print("거스름돈 계산")
x = int(input("물건값 : "))
y = int(input("받은돈 : "))
z = y-x

a = z//10000
b = (z-a*10000)//5000
c = (z-a*10000-b*5000)//1000
z = a*10000+b*5000+c*1000

if z < 0:
    print("금액이 부족합니다.")

elif z >= 0:
    print("거스름돈은 1만원권 {}장, 5천원권 {}장, 1천원권 {}장".format(a,b,c))
    print("총 {}원입니다".format(z))


# 50,000 - 12,000 = 38,000
# 38,000 = 10,000*3 + 5,000*1 + 1,000*3