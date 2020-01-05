score1, score2, score3, score4, score5 = input().split()

score1 = float(score1)
score2 = float(score2)
score3 = float(score3)
score4 = float(score4)
score5 = float(score5)

max_score = max(score1, score2, score3, score4, score5)
min_score = min(score1, score2, score3, score4, score5)

total_score = (score1 + score2 + score3 + score4 + score5) - (max_score + min_score)
avg_score = total_score / 3

print(f'{avg_score:.2f}')  # 소수점 두 번째 자리까지 출력