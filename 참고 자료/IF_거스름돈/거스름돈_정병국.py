money = int(input("받은돈 : "))
price = int(input("물건값 : "))

change = money - price
change_1 = change // 10000
change_2 = (change - change_1 * 10000 ) // 5000 
chage_3 = (change - (change_1 * 10000) - (change_2 * 5000 ) ) // 1000

if money < price:
    print('돈이 부족합니다')
else:
    print('거스름돈은 {}이며, 만원짜리 {}장, 오천원짜리 {}장, 천원짜리 {}장 입니다'.format(change, change_1,change_2,chage_3))