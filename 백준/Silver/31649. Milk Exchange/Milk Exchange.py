n,m = map(int,input().split())
direction = input()
bucket_capacities = list(map(int,input().split()))

in_degree = [0] * n
total_milk = sum(bucket_capacities)
move_idx = 0

# 각 소마다 몇 번 우유를 받는지 체크
for idx, dir in enumerate(direction):
    # 왼쪽으로 전달하는 경우
    if dir == 'L':
        if idx == 0:
            move_idx = n - 1
        else:
            move_idx = idx - 1
    # 오른쪽으로 전달하는 경우
    elif dir == 'R':
        if idx == n - 1:
            move_idx = 0
        else:
            move_idx = idx + 1

    in_degree[move_idx] += 1

# 진입차수가 0인 노드 찾기
start_cows = {}
for i in range(n):
    if in_degree[i] == 0:
        start_cows[i] = 0

# 0인 노드에서 출발해서 우유 누적시키기
for key in start_cows.keys():
    cow = key
    milk = 0
    # 진입차수가 2라면 이동 끝
    while in_degree[cow] < 2:
        milk += bucket_capacities[cow]
        # 왼쪽으로 전달하는 경우
        if direction[cow] == 'L':
            if cow == 0:
                cow = n - 1
            else:
                cow -= 1
        # 오른쪽으로 전달하는 경우
        elif direction[cow] == 'R':
            if cow == n - 1:
                cow = 0
            else:
                cow += 1
    start_cows[key] = milk

# 손실된 우유 계산
lost_milk = 0
for milk in start_cows.values():
    if milk >= m:
        lost_milk += m
    else:
        lost_milk += milk

print(total_milk - lost_milk)
