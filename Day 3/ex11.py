year = int(input('연도를 입력하세요 : '))
is_leap = False

if year % 4 == 0:
    if year % 100 != 0: is_leap = True  # 4로 나눠지지만 100으로 나눠지지 않아야 윤년이다. 2100년은 4로 나눠지면서 100으로 나눠지기 때문에 윤년이 아니다
    
if year % 400 == 0: is_leap = True  # 그러나 400으로 나눠지면 윤년이다

if is_leap: print("윤년")
elif not is_leap: print("윤년아님")
