n, q = map(int,input().split())
farms = list(map(int,input().split()))
time = list(map(int,input().split()))

diff = [0] * n
# Bessie가 일어날 수 있는 시간 구하기
for i in range(n):
    diff[i] = farms[i] - time[i]
diff.sort(reverse=True)

for i in range(q):
    # 방문가능한 농장 수, 일어나는 시간
    v, s = map(int,input().split())
    if diff[v - 1] > s:
        print('YES')
    else:
        print('NO')

