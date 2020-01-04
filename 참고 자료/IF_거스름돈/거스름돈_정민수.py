input_money = int(input('투입한 돈:  '))
input_price = int(input('물건 값:  '))
rest_money = input_money - input_price
rest_thousand = rest_money//1000
rest_fivehundred = (rest_money%1000)//500
rest_hundred = ((rest_money%1000)%500)//100
print('거스름돈은 1000원 짜리 {}개, 500원짜리 {}개, 100원짜리 {}개입니다.'.format(rest_thousand, rest_fivehundred, rest_hundred))

