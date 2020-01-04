# 리듬체조 점수 구하기 
scores = [0, 0, 0, 0, 0]

for i in range(len(scores)) :
    scores[i] = float(input(" 점수를 입력하세요 >"))

for x in reversed(range(len(scores))):
        for i in range(x):
            if scores[i] > scores[i+1]:
                scores[i], scores [i+1] = scores[i+1], scores[i]

sum = float(0)

for i in range(1,len(scores)-1,1) :
    sum = sum + scores[i]

avg = float(sum / 3)
print (avg) 
