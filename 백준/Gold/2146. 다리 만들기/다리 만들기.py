from collections import deque

# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

n = int(input())
graph = [[] * n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))


def island_numbering(y, x, num):
    queue = deque()
    queue.append((y, x))
    graph[y][x] = num

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 범위 체크
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1:
                graph[ny][nx] = num
                queue.append((ny, nx))

def building_bridge(num):
    dist = [[0] * n for _ in range(n)]
    # num 번호를 가진 대륙 찾기
    queue = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == num:
                queue.append((i, j))

    # 다리 놓으면서 거리 찾기
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 범위 체크
            if 0 <= ny < n and 0 <= nx < n:
                # 다른 도시를 만났을 경우 리턴
                if graph[ny][nx] != num and graph[ny][nx] != 0:
                    return dist[y][x]

                # 아직 가지 않은 바다인 경우
                if graph[ny][nx] == 0 and dist[ny][nx] == 0:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny, nx))
# ====================== main ======================

# 육지 찾아서 섬 번호 넘버링
num = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            island_numbering(i,j,num)
            num += 1

# 각 섬마다 다리 놓기
result = 10001
for i in range(2, num):
    distance = building_bridge(i)
    result = min(result,distance)

print(result)