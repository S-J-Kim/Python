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

# 홀/짝 구분하는 조건문 실습
import math

x = int(input("정수를 입력하세요 : "))

# 짝수
if x % 2 == 0:
    print('입력하신 숫자 {}는 짝수입니다.'.format(x))

# 홀수
else:
    print('입력하신 숫자 {}는 홀수입니다.'.format(x))

# 홀/짝 구분하는 조건문 실습2 
# 마지막이 2/4/6/8/0 로 끝나는 숫자의 경우 다시 한번 확인
# if 조건문 예시 확인
x = int(input("정수를 입력하세요 :"))

# 홀/짝 구분하는 조건문 예시문

# 입력을 받습니다.
number = input('정수 입력:')
number = int(number)

# 문자열로 변환
number = str(number)

# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_number = int(last_character)

#짝수 확인
if last_number == 0 \
    or last_number == 2\
    or last_number == 4\
    or last_number == 6\
    or last_number == 8:

    print('짝수입니다.')

# 홀수 확인
if last_number == 1\
    or last_number == 3\
    or last_number == 5\
    or last_number ==7\
    or last_number ==9:

    print('홀수입니다.')

# 홀/짝 구분하는 예시문2

number = input('정수입력 : ')
last_character = number[-1]

if last_character in "02468":
    print('짝수입니다.')

if last_character in "13579":
    print('홀수입니다.')

"""

# 학점과 학생평가에 대하여 조건문으로 구현하시오. 실습
import math

x = float(input('학점을 입력하시오. :'))

# 신
if x == 4.5:
    print('학생의 학점은 {}점으로 신입니다.'.format(x))

# 교수님의 사랑
elif 4.2 <= x < 4.5:
    print('학생의 학점은 {}점으로 교수님의 사랑입니다.'.format(x))

# 현 체제의 수호자
elif 3.5 <= x < 4.2:
    print('학생의 학점은 {}점으로 현 체제의 수호자입니다.'.format(x))

# 일반인
elif 2.8 <= x < 3.5:
    print('학생의 학점은 {}점으로 일반인입니다.'.format(x))

# 일탈을 꿈꾸는 소시민
elif 2.3 <= x < 2.8:
    print('학생의 학점은 {}점으로 일탈을 꿈꾸는 소시민입니다.'.format(x))

# 오락문화의 선구자
elif 1.75 <= x < 2.3:
    print('학생의 학점은 {}점으로 오락문화의 선구자입니다.'.format(x))

#불가촉천민
elif 1.0 <= x < 1.75:
    print('학생의 학점은 {}점으로 불가촉천민입니다.'.format(x))

#자벌레
elif 0.5 <= x <1.0:
    print('학생의 학점은 {}점으로 자벌레입니다.'.format(x))

#플랑크톤
elif 0 < x < 0.5:
    print('학생의 학점은 {}점으로 플랑크톤입니다.'.format(x))

#시대를 앞서가는 혁명의 씨앗
else:
    print('학생의 학점은 {}점으로 시대를 앞서가는 혁명의 씨앗입니다.'.format(x))

