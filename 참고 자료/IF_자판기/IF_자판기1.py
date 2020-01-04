# 자판기 프로그램


print ('사이다-700원, 콜라-800원, 물-1200원')
money = input('돈을 넣어주세요 : ')
money = int(money)

buy = input('선택) 1-사이다 2-콜라 3-물 : ')
buy = int(buy)

if buy == 1 :
    buy = 700
    product = '사이다'
elif buy == 2 :
    buy = 800
    product = '콜라'
elif buy == 3 :
    buy = 1200
    product = '물'
else :
    pass


change = money - buy

if change < 0 :
    print ('{}은 {}원 입니다. {}원을 더 넣어주세요'.format(product, buy, abs(change)))
    print ('10초 이내 {}원을 입력하지 않으면 {}원을 반환합니다. '.format(abs(change), money))
else :
    print ('{}이 나왔습니다. 덜컹'.format(product))
    print ('잔돈 {}원을 반환합니다.'.format(change))

