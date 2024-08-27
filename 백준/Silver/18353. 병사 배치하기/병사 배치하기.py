n = int(input())
soldier = list(map(int,input().split()))

# LIS 알고리즘 사용을 위해 배열 뒤집기
soldier.reverse()
dp = [1] * n

for i in range(1, n):
    # 배열 가장 첫 요소부터 돌면서 증가하는 배열의 길이 갱신
    for j in range(0, i):
        if soldier[i] > soldier[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(soldier)
# dp[n - 1]에 가장 큰 증가하는 부분 수열의 길이가 저장되어있으므로
# 총 length - dp[n - 1]
print(n - max(dp))