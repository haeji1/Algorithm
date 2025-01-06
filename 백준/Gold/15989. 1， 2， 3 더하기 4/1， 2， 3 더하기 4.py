t = int(input())

# 모든 수는 1로 합을 구성할 수 있다
dp = [1] * 10001
for i in range(2, 10001):
    dp[i] += dp[i - 2]
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for tc in range(t):
    n = int(input())
    print(dp[n])