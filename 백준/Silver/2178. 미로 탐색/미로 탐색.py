from collections import deque

# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
visited = [[0] * m for _ in range(n)]
def bfs(y,x):
    queue = deque()
    queue.append((y,x))

    # 방문처리
    visited[y][x] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 범위 체크
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))

bfs(0,0)
print(visited[n - 1][m - 1])