def solve():
    string = input()
    code = []

    for val in string:
        code.append(int(val))

    dp = [1 for _ in range(len(code) + 1)]

    if code[0] == 0: return 0
    
    dp[1] = 1

    for i in range(2, len(code) + 1):

        num = code[i - 2] * 10 + code[i - 1]
        
        if not num: return 0

        if 1 <= num < 10:
            dp[i] = dp[i - 3]

        elif 10 <= num <= 26:
            if not num % 10:
                dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
            
        else:
            if not num % 10:
                return 0
            else:
                dp[i] = dp[i - 1]
        
    return dp[len(code)]
    
print(solve() % 1000000)
