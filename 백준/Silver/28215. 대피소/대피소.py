from itertools import combinations
n,k = map(int,input().split())
house = []
for _ in range(n):
    x,y = map(int,input().split())
    house.append([x,y])
    
# 모든 집과의 거리가 가장 가까운 대피소 찾기
list = [[] for _ in range(n)]
result = float('INF')
for c in combinations(house, k):
    tmp = []
    max_val = 0
    for h in range(n):
        home = house[h]
        min_val = 99999999
        for cc in c:
            distance = []
            tmp_val = abs(home[0] - cc[0]) + abs(home[1] - cc[1])
            min_val = min(min_val, tmp_val)
        max_val = max(min_val, max_val)
    result = min(max_val, result)

print(result)