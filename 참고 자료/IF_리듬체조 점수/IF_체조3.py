s1 = float(input("점수를 입력: "))
s2 = float(input("점수를 입력: "))
s3 = float(input("점수를 입력: "))
s4 = float(input("점수를 입력: "))
s5 = float(input("점수를 입력: "))

score = (s1, s2, s3, s4, s5)

max_score = s1
min_score = s1

if s2 >= max_score :
    max_score = s2
elif s2 <= min_score :
     min_score = s2
if s3 >= max_score :
    max_score = s3
elif s3 <= min_score :
     min_score = s3
if s4 >= max_score :
    max_score = s4
elif s4 <= min_score :
     min_score = s4
if s5 >= max_score :
    max_score = s5
elif s5 <= min_score :
     min_score = s5

print("최고점수는 {}점이고, 최저점수는 \
      {}점입니다".format(max_score, min_score))


total = (s1 + s2 + s3 + s4 + s5) - max_scroe - min_score

avr = total / 3

print("총점수는 {}이고, 평균점수는 {:.3f}입니다".format(total, avr))






