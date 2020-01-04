# 짝수 구별
x=int(input("숫자를 입력하세요: "))
if x %2 == 0:
    print('{}는 짝수입니다.'.format(x))
else:
    print('{}는 홀수 입니다.'.format(x))



a=(input("숫자를 입력하세요: "))
x=[2,4,6,8,0]
if int(a[-1]) in x:
   print('{}는 짝수입니다.'.format(a))
else:
    print('{}는 홀수 입니다.'.format(a))    