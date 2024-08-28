from collections import deque
# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = [[0] * m for _ in range(n)]

start_y, start_x = map(int,input().split())
end_y, end_x = map(int,input().split())

# -1해서 배열 인덱스와 맞추기
start_y -= 1
start_x -= 1
end_y -= 1
end_x -= 1


def go_to_end():
    global start_y, start_x, end_y, end_x
    queue = deque()
    queue.append((start_y, start_x))
    visited[start_y][start_x] = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                # 새로 간 곳이 이미 방문한 곳이라면 도착지인지 체크
                if visited[ny][nx] == 1:
                    if ny == end_y and nx == end_x:
                        return 'YES'
                    else:
                        continue
                # 새로 방문한 곳이 이미 꺠져있는 얼음이라면
                if graph[ny][nx] == 'X':
                    if ny == end_y and nx == end_x:
                        return 'YES'
                    else:
                        continue
                visited[ny][nx] = 1
                queue.append((ny, nx))

    return 'NO'


print(go_to_end())