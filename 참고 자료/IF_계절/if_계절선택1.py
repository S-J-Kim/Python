import datetime
now = datetime.datetime.now()

now_month = now.month;

season = ["봄", "여름", "가을", "겨울"]

if 2 < now_month <= 5 :
    print(season[0])
elif 5 < now_month <= 8 :
    print(season[1])
elif 8 < now_month <= 11 :
    print(season[2])
elif (0 < now_month <= 2 or now_month == 12) :
    print(season[3])
    




