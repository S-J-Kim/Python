#다섯 심판의 점수를 입력받는다.

a1 = float(input('1번 점수 입력해주세요 : '))
a2 = float(input('2번 점수 입력해주세요 : '))
a3 = float(input('3번 점수 입력해주세요 : '))
a4 = float(input('4번 점수 입력해주세요 : '))
a5 = float(input('5번 점수 입력해주세요 : '))

score = (a1, a2, a3, a4, a5)

# 최대값과 최소값을 구한다.

max = min = a1

if a2 >= max:
    max = a2
if a2 <= min:
    min = a2

if a3 >= max:
    max = a3
if a3 <= min:
    min = a3

if a4 >= max:
    max = a4
if a4 <= min:
    min = a4

if a5 >= max:
    max = a5
if a5 <= min:
    min = a5

print()
print('최고점은 {:.3f}이고, 최저점은 {:.3f}입니다.'.format(max,min))

# 평균값을 구한다.

average=(((a1 + a2 + a3 + a4 + a5) - max - min)/3)


print()
print("최종점수는 {:.3f} 입니다".format(average))

#{:.3f} 소수점 세번째 자리까지 출력

print()
input("엔터를 눌러 창을 닫으세요")