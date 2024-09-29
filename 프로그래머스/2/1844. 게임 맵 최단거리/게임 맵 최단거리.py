from collections import deque
# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    def bfs(y,x):
        queue = deque()
        queue.append((y,x))
        visited[y][x] = 1
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                    if not visited[ny][nx]:
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny,nx))
        if not visited[n - 1][m - 1]:
            return -1
        else:
            return visited[n - 1][m - 1]

    answer = bfs(0,0)
    return answer