n, k = map(int,input().split())
dp = [[] for _ in range(12)]
dp[1] = ["1"]
dp[2] = ["1+1","2"]
dp[3] = ["1+1+1","1+2","2+1","3"]

for i in range(4, 12):
    for j in dp[i - 1]:
        dp[i].append(j+"+1")
    for j in dp[i - 2]:
        dp[i].append(j+"+2")
    for j in dp[i - 3]:
        dp[i].append(j+"+3")

# k번째 식 존재하는지 확인
if len(dp[n]) >= k:
    print(sorted(dp[n])[k - 1])
else:
    print(-1)