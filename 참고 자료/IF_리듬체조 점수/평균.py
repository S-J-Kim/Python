#다섯명의 점수 중 최고 최저 버리고
#입력받은 j1을 최고이자 최저로 선언
#나머지 중간 세명의 평균 출력

s1 = float(input("점수를 입력하세요 s1 : "))
s2 = float(input("점수를 입력하세요 s2 : "))
s3 = float(input("점수를 입력하세요 s3 : "))
s4 = float(input("점수를 입력하세요 s4 : "))
s5 = float(input("점수를 입력하세요 s5 : "))

score = (s1, s2, s3, s4, s5)
#score = [0,0,0,0,0]
#score = input().


#max, min
#max_score = max(score)
#min_score = min(score)
max_score = s1
min_score = s1
#max = min = s1 로도 표현가능


if s2 >= max_score:
    max_score = s2
if s2 <= min_score:
    min_score = s2

if s3 >= max_score:
    max_score = s3
if s3 <= min_score:
    min_score = s3

if s4 >= max_score:
    max_score = s4
if s4 <= min_score:
    min_score = s4

if s5 >= max_score:
    max_score = s5
if s5 <= min_score:
    min_score = s5

print("최고점은 {}점, 최저점은 {}점".format(max_score, min_score))

#총합
total = s1
total += s2
total += s3
total += s4
total += s5
#total = s1 + s2 + s3 + s4 + s5

'''
for i in (1,2,3,4):
    total += score[i]
'''

sum = total - (max_score + min_score)

print("다섯명의 총점은 {}점이고 가운데 세 명의 평균은 {:.3f}점".format(total, sum/3))
