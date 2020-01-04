import datetime
now = datetime.datetime.now()
hour = now.hour
print(hour)
if 0 <= hour < 12: 
    print('현재 시간은 {}시, 오전입니다'.format(hour))
else:
    print('현재 시간은 {}시, 오후입니다'.format(hour))