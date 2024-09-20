from collections import deque
# 말의 움직임
horse = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,-2],[2,-1],[2,1],[1,2]]

# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

k = int(input())
w, h = map(int,input().split())
graph = []
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
for _ in range(h):
    graph.append(list(map(int,input().split())))

def bfs(y,x, cnt):
    queue = deque()
    queue.append((y,x,cnt))
    visited[y][x][cnt] = 1
    while queue:
        y, x, cnt = queue.popleft()
        # 종료조건
        if y == h - 1 and x == w - 1:
            return visited[y][x][cnt] - 1
        # 원숭이 이동
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if graph[ny][nx] == 0 and not visited[ny][nx][cnt]:
                    visited[ny][nx][cnt] = visited[y][x][cnt] + 1
                    queue.append((ny, nx, cnt))

        # 말 이동
        if cnt < k:
            for (hy, hx) in horse:
                ny = y + hy
                nx = x + hx
                if 0 <= ny < h and 0 <= nx < w:
                    if graph[ny][nx] == 0 and not visited[ny][nx][cnt + 1]:
                        visited[ny][nx][cnt + 1] = visited[y][x][cnt] + 1
                        queue.append((ny, nx, cnt + 1))

    return -1

print(bfs(0,0,0))
