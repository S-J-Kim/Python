pay = int(input("얼마 받았습네까? "))
price = int(input("물건값은 얼마입네까? "))
change = pay-price

won1000 = change//1000
won500 = (change%1000)//500
won100 = ((change%1000)//500)%100

print(('''"1000원짜리 지폐 : {}장"
"500원짜리 동전 : {}개"
"100원짜리 동전 : {}개"''').format(won1000,won500,won100))