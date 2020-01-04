#만, 천원 몇장씩?

cost = int(input("물건값은 얼마인가? : "))
money = int(input("얼마를 내실건가요? : "))
change = money - cost
if change < 0:
    print("돈이 모자랍니다")
else:
    green = change//10000
    red = (change//1000)%10
    print("만원 {}장, 천원 {}장".format(green, red))
    yellow = red//5
    red = red % 5

    print("거스름돈은 {}원이므로 만원 {}장, 오천원 {}장, 천원{}장".format(change, green, yellow, red))

