print('x를 입력하세요')
print('입력하지 않고 엔터를 치시면 종료됩니다.')
x = input('x : ')
x = int(x)

if x % 2 == 0:
    print('x 는 짝수입니다.')
if x % 2 == 1:
    print('x 는 홀수입니다.')