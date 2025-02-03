t = int(input())
dp = [1] * 11
for i in range(11):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for _ in range(t):
    n = int(input())
    print(dp[n])