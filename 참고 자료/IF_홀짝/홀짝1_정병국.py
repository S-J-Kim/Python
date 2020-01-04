a = int(input("판별할 숫자를 입력하세요 : \n"))

b = a%2

if b:
     print('{}은 홀수입니다'.format(a))


if b==0:
    print('{}은 짝수입니다'.format(a))
