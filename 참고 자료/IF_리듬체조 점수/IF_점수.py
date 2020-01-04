# 다섯명의 심판의 점수를 입력받아 평균 구하기
# 조건1. 최대점수와 최저 점수는 제외한다.
# 조건2. 점수는 실수로 입력한다.(float)

# j1,j2,j3,j4,j5 = input("점수 다섯개: ").split()

j1 = float(j1)
j2 = float(j2)
j3 = float(j3)
j4 = float(j4)
j5 = float(j5)







j1 = float(input("점수: "))
j2 = float(input("점수: "))
j3 = float(input("점수: "))
j4 = float(input("점수: "))
j5 = float(input("점수: "))

score = (j1, j2, j3, j4, j5)


# 최대점수, 최저점수 구하기 : max, min

max_score = j1
min_score = j1






# max_score  = min_score = j1 와 같은 형식으로도 가능하다.


if j2 > max_score :
    max_score = j2

if j2 < min_score :
    min_score = j2

if j3 > max_score :
    max_score = j3

if j3 < min_score :
    min_score = j3

if j4 > max_score :
    max_score = j4

if j4 < min_score :
    min_score = j4

if j5 > max_score :
    max_score = j5

if j5 < min_score :
    min_score = j5

print("최고점은 {}, 최저점은 {}입니다".format(max_score,min_score)



# 합계, 평균 구하기
sum = (j1 + j2 + j3 + j4 + j5)
a = sum - (max_score + min_score)/3

print("다섯명의 총점은 {} 평균점수는 {:.5f}점 입니다".format(sum, a)









      








