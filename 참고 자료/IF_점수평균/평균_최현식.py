# 다섯 심판 점수 입력
# 최고점, 최저점 구한다
# (총점 - 최고점 - 최저점) /3 의 평균
# score = [0,0,0,0,0]
# score = input("다섯명의 평가 점수를 입력해주세요 << ").split()
# a = int(score[0]) +int(score[1]) +int(score[2]) +int(score[3]) +int(score[4]) 
# b = int(max(score))
# c = int(min(score))
# d = int((a-b-c)/3)
# print("총점:{}".format(a))
# print("최고점:{}".format(b))
# print("최저점:{}".format(c))
# print("계산식:({} - {} - {}) / 3 = {}".format(a,b,c,d))
# print("최종 점수는 {}입니다.".format(d))

score = [0,0,0,0,0]
score = input("다섯명의 평가 점수를 입력해주세요 << ").split()
# 총점
a = int(score[0]) +int(score[1]) +int(score[2]) +int(score[3]) +int(score[4]) 
# print("총점:{}".format(a))
b = score[0]
if int(b < score[1]):
    b = score[1]
if int(b < score[2]):
    b = score[2]
if int(b < score[3]):
    b = score[3]
if int(b < score[4]):
    b = score[4]
# print("최고점:{}".format(b))
c = score[0]
if int(c > score[1]):
    c = score[1]
if int(c > score[2]):
    c = score[2]
if int(c > score[3]):
    c = score[3]
if int(c > score[4]):
    c = score[4]
# print("최저점:{}".format(c))
d = float((int(a)-int(b)-int(c))/3)
print("계산식:({} - {} - {}) / 3 = {}".format(a,b,c,d))
print("최종 점수는 {}입니다.".format(d))