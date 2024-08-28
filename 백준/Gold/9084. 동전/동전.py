t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int,input().split()))
    m = int(input())

    # 만들어야 하는 금액 크기의 dp 테이블 생성
    dp = [0] * (m + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, m + 1):
            if dp[i - coin] != 0:
                dp[i] += dp[i - coin]
    print(dp[m])