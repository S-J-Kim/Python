score1 = float(input("1번째 심판의 점수를 입력하세요 : "))
print(score1)
score2 = float(input("2번째 심판의 점수를 입력하세요 : "))
print(score2)
score3 = float(input("3번째 심판의 점수를 입력하세요 : "))
print(score3)
score4 = float(input("4번째 심판의 점수를 입력하세요 : "))
score5 = float(input("5번째 심판의 점수를 입력하세요 : "))

score_list = [score1, score2, score3, score4, score5]

max_score = max(score_list)
min_score = min(score_list)

print('최고점수는 {}입니다.'.format(max_score))
print('최저점수는 {}입니다.'.format(min_score))

sum = 0

for x in range(5):
     sum += score_list[x]
sum = sum - max_score - min_score
    
average = sum / 3

print("평균점수는 {}점입니다.".format(average))

        
