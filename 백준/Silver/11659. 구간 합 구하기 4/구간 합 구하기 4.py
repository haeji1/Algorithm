n, m = map(int,input().split())
array = list(map(int,input().split()))
prefix_sum = [0] * (n + 1)
prefix_sum[1] = array[0]
for i in range(2, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + array[i - 1]
for _ in range(m):
    i,j = map(int,input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
