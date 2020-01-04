"""
x = 10
if x == 10:
    print('10입니다.')

x = 10
if x == 10:
print('10입니다.')    # 들여쓰기를 하지않는 잘못된 예

if x = 10:
    print('10입니다.')  # = 과 == 혼동하지 말것!

x = 10
if x == 10:
    print('x에 들어있는 숫자는')
        print('10입니다.')                       # 잘못된 들여쓰기의 예

x = 10
if x == 10:
    print('x에 들어있는 숫자는')          # 참이여서 출력 후
print('10입니다.')                               # 독립적으로 출력

x = 5
if x == 10:
    print('x에 들어있는 숫자는')          # 거짓이여서 출력 안됨
print('10입니다.')                               # 독립적으로 출력

x = 15
if x >= 10:
    print('10이상입니다.')

    if x == 15:
        print('15입니다.')

    if x == 20:
        print('20입니다.')

# 한문장 만들기 실습

x = 15
if x>= 10 x == 15:
    print('10 이상이며 15입니다.')     # 뭐지 뒤에서 다시 한다고 함


# 계절 출력 복습

import datetime
now = datetime.datetime.now()

# 봄

if 3<= now.month <=5:
    print('현재 {}월로 계절은 봄입니다.'.format(now.month))

# 여름

if 6<= now.month <=8:
    print('현재 {}월로 계절은 여름입니다.'.format(now.month))

# 가을

if 9 <= now.month <=11:
    print('현재 {}월로 계절은 가을입니다.'.format(now.month))

# 겨울
else:
    print('현재 {}월로 계절은 겨울입니다.'.format(now.month))

"""

# 홀/짝 구분하는 조건문 실습
import math

x = int(input("정수를 입력하세요 : "))

# 짝수
if x % 2 == 0:
    print('입력하신 숫자 {}는 짝수입니다.'.format(x))

# 홀수
else:
    print('입력하신 숫자 {}는 홀수입니다.'.format(x))





