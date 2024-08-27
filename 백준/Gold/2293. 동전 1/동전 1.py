n, k = map(int,input().split())
coins = []
dp = [0] * (k + 1)

for _ in range(n):
    coins.append(int(input()))

# 초기화 위헤서 dp[0]을 1로 세팅
dp[0] = 1
for coin in coins:
    for i in range(coin, k + 1):
        if dp[i - coin] != 0:
            dp[i] = dp[i] + dp[i - coin]

print(dp[k])