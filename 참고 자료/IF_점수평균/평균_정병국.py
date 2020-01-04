score_1 = int(input("1번 선수의 점수 : "))
score_2 = int(input("2번 선수의 점수 : "))
score_3 = int(input("3번 선수의 점수 : "))
score_4 = int(input("4번 선수의 점수 : "))
score_5 = int(input("5번 선수의 점수 : "))

score_list = (score_1, score_2, score_3, score_4, score_5)

'''
쉽게 푸는 방법
rank_1 = max(score_list)
rank_5 = min(score_list)
'''
#rank_1 = 1등
#rank_2 = 2등
#rank_2 = 3등
#rank_2 = 4등
#rank_2 = 5등

# 1등 구하기
####################
rank_1 = score_1

if rank_1 > score_2 :
    pass
else :
    rank_1 = score_2

if rank_1 > score_3:
    pass
else:
    rank_1 = score_3

if rank_1 > score_4:
    pass
else:
    rank_1 = score_4

if rank_1 > score_5:
    pass
else:
    rank_1 = score_5

# 꼴지 구하기

rank_5 = score_1

if rank_5 < score_2:
    pass
else:
    rank_5 = score_2

if rank_5 < score_3:
    pass
else:
    rank_5 = score_3

if rank_5 < score_4:
    pass
else:
    rank_5 = score_4

if rank_5 < score_5:
    pass
else:
    rank_5 = score_5


total_score = score_1 + score_2 + score_3 + score_4 + score_5

average_total_score = total_score - rank_1 - rank_5

average = average_total_score / 3

print ('최고점은 {} 이고 최저점은 {}이며 평균은 {:.3f}입니다'.format(rank_1,rank_5,average))
