#심판점수 입력
j1 = int(input('심판1의 점수를 입력하세요: '))
j2 = int(input('심판2의 점수를 입력하세요: '))
j3 = int(input('심판3의 점수를 입력하세요: '))
j4 = int(input('심판4의 점수를 입력하세요: '))
j5 = int(input('심판5의 점수를 입력하세요: '))

#최대값, 최소값 지정
max = min = j1

if j2 > max:
    max = j2
elif j2 < min:
    min = j2
if j3 > max:
    max = j3
elif j3 < min:
    min = j3
if j4 > max:
    max = j4
elif j4 < min:
    min = j4
if j5 > max:
    max = j5
elif j5 < min:
    min = j5

final = (j1 + j2 + j3 + j4 + j5 - max - min)/3

#최종점수 
print('최종점수는 {:.3f}입니다'.format(final))

