import datetime

now = datetime.datetime.now()


if now.hour < 12 :
	print("오전 {}시 {}분 입니다".format(now.hour, now.minute))

else :
    print("오후 {}시 {}분 입니다".format(now.hour, now.minute))
