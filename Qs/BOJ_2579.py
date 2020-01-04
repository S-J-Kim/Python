n_of_stairs = int(input())

def solve(stairs):
    score = []
    max_score = [-1 for _ in range(stairs)]
    
    for i in range(stairs):
        score.append(int(input()))
    
    if stairs == 1: return score[0]
    if stairs == 2: return score[0] + score[1]
    if stairs == 3: return max(score[0] + score[2], score[1] + score[2])

    max_score[0] = score[0]
    max_score[1] = score[0] + score[1]
    max_score[2] = max(score[0] + score[2], score[1] + score[2])
    
    for i in range(3, stairs):
        max_score[i] = max(max_score[i - 3] + score[i - 1] + score[i], max_score[i - 2] + score[i])

    return max_score[stairs - 1]
    
print(solve(n_of_stairs))