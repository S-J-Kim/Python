j_1 = float(input("1번 심판의 점수를 입력하세요"))
j_2 = float(input("2번 심판의 점수를 입력하세요"))
j_3 = float(input("3번 심판의 점수를 입력하세요"))
j_4 = float(input("4번 심판의 점수를 입력하세요"))
j_5 = float(input("5번 심판의 점수를 입력하세요"))

list = [j_1, j_2, j_3, j_4, j_5]
print("최고 점수는", max(list), "입니다.")
print("최저 점수는", min(list), "입니다.")


max = min = j_1
if j_2 > max:
    max = j_2
elif j_2 < min:
    min = j_2

if j_3 > max:
    max = j_3
elif j_3 < min:
    min = j_3

if j_4 > max:
    max = j_4
elif j_4 < min:
    min = j_4

if j_5 > max:
    max = j_5
elif j_5 < min:
    min = j_5

score = (j_1 + j_2 + j_3 + j_4 + j_5 - max - min) / 3
print("최종 평균점수는 {:.3f}".format(score))