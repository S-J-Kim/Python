'''
N, k = map(int, input().split())

room = [list(map(int, input().split())) for lv in range(N + 1)]
room.insert(0, [0, 0])

dp = [[[0 for door in range(202)] for i in range(202)] for dep in range(3)]

dp[1][1][1] = room[1][0]
dp[2][1][1] = room[1][1]
dp[0][1][0] = room[1][0] + room[1][1]

for i in range(2, N + 1):
    for j in range(k + 1):
        if j >= 1:
            dp[2][i][j] = max(dp[0][i - 1][j - 1], dp[2][i - 1][j - 1]) + room[i][0]
            dp[1][i][j] = max(dp[0][i - 1][j - 1], dp[1][i - 1][j - 1]) + room[i][1]
        
        if not j == i:
            dp[0][i][j] = max(dp[0][i - 1][j], dp[1][i - 1][j], dp[2][i - 1][j]) + room[i][0] + room[i][1]
        
print(max(dp[0][N][k], dp[1][N][k], dp[2][N][k]))
'''

N, k = map(int, input().split())

room = [list(map(int, input().split())) for lv in range(N + 1)]
room.insert(0, [0, 0])

dp = [[[0 for door in range(k + 2)] for i in range(N + 1)] for dep in range(3)]

dp[1][1][1] = room[1][0]
dp[2][1][1] = room[1][1]
dp[0][1][0] = room[1][0] + room[1][1]

for i in range(2, N + 1):
    for j in range(k + 1):
        dp[2][i][j] = max(dp[0][i - 1][j - 1], dp[2][i - 1][j - 1]) + room[i][0]
        dp[1][i][j] = max(dp[0][i - 1][j - 1], dp[1][i - 1][j - 1]) + room[i][1]
        dp[0][i][j] = max(dp[0][i - 1][j], dp[1][i - 1][j], dp[2][i - 1][j]) + room[i][0] + room[i][1]
        
print(max(dp[0][N][k], dp[1][N][k], dp[2][N][k]))