# //2, //3, -1
n = int(input())
dp = [[0, []] for _ in range(n + 1)]

def make_one(n):
    dp[1][0] = 0
    dp[1][1] = [1]

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + 1
        # 연산 과정 파악 위한 2차원 배열
        dp[i][1] = dp[i - 1][1] + [i]
        if not i % 3:
            if dp[i][0] > dp[i//3][0] + 1:
                dp[i][0] = dp[i//3][0] + 1
                dp[i][1] = dp[i//3][1] + [i]
        if not i % 2:
            if dp[i][0] > dp[i//2][0] + 1:
                dp[i][0] = dp[i//2][0] + 1
                dp[i][1] = dp[i//2][1] + [i]

    return dp[n]

print(make_one(n)[0])
print(*reversed(dp[n][1]))