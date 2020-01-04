import datetime

now = datetime.datetime.now()

month = now.month

if 3 <= month <= 6: print('1학기')
if 7 <= month <= 8: print('1학기 계절학기')
if 9 <= month <= 12: print('2학기')
if 1 <= month <= 2: print('2학기 계절학기')
