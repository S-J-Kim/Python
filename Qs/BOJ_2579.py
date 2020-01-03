n_of_stairs = int(input())

scores = []
mxs = [-1 for _ in range(n_of_stairs + 3)]

for i in range(0, n_of_stairs):
    scores.append(int(input()))
mxs[0] = scores[0]
mxs[1] = scores[0] + scores[1]
mxs[2] = max(mxs[0] + scores[2], mxs[1] + scores[2])

for i in range(3, n_of_stairs):
    mxs[i] = max(mxs[i - 3] + scores[i - 1] + scores[i], mxs[i - 2] + scores[i])
    
print(mxs[n_of_stairs - 1])