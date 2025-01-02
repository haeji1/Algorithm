n, m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

# 2차원 배열 누적합 구하기
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + array[i - 1][j - 1]

# 인덱스별 부분합 구하기
for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)