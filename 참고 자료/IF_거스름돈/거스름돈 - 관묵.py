x=int(input("구매 금액: "))
y=int(input("제출 금액: "))
xy = y-x

print("거스름돈: {}원".format(xy))

if xy >= 10000:
    th_10 = xy // 10000
    th_5 = (xy - (th_10*10000)) // 5000
    th_1 = (xy - (th_10*10000) - (th_5*5000)) // 1000
    print("만원:{0}장, 오천원:{1}장, 천원:{2}장".format(th_10,th_5,th_1))
elif xy >= 5000:
    th_1 = (xy - 5000) // 1000
    print("오천원:1장, 천원:{}장".format(th_1))
elif xy > 0:
    th_1 = xy // 1000
    print("천원:{}장".format(th_1))
else :
    print("거스름돈이 없습니다.")


