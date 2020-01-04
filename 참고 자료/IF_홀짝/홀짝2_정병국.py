a = int(input("판별할 숫자를 입력하세요:\n"))

b = a%10

if b == (2 or 4 or 6 or 8 or 0):
    print('{}은 짝수입니다'.format(a))

else:
    print('{}은 홀수입니다'.format(a))