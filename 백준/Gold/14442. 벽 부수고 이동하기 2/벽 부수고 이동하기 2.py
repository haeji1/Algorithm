from collections import deque
# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]
n, m, k = map(int,input().split())

graph = [[] * m for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

# print(visited)
for i in range(n):
    graph[i] = list(map(int,input()))

def bfs(y, x):
    queue = deque()
    w = 0
    queue.append((y,x,w))
    # 시작하는 칸 포함
    visited[y][x][w] = 1

    while queue:
        y, x, w = queue.popleft()

        if y == n - 1 and x == m - 1:
            return visited[y][x][w]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위체크
            if 0 <= ny < n and 0 <= nx < m:
                # 벽울 부수지 않아도 되는 경우
                if graph[ny][nx] == 0 and not visited[ny][nx][w]:
                    visited[ny][nx][w] = visited[y][x][w] + 1
                    queue.append((ny, nx, w))
                # 벽을 부수는 경우
                elif graph[ny][nx] == 1 and w < k and not visited[ny][nx][w + 1]:
                    visited[ny][nx][w + 1] = visited[y][x][w] + 1
                    queue.append((ny, nx, w + 1))

    return -1

print(bfs(0,0))