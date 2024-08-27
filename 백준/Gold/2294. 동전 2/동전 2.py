n, k = map(int,input().split())
INF = 100001
dp = [INF] * (k + 1)
coins = []

dp[0] = 0
for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for i in range(coin, k + 1):
        if dp[i - coin] != INF:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k]) if dp[k] != INF else print(-1)