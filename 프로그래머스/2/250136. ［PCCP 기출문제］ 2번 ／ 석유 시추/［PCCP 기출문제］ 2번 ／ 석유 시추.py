from collections import deque
# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    oil_size = dict()
    
    # bfs로 레벨링 + 석유크기 저장
    cnt = 2
    for j in range(m):
        tmp = 0
        for i in range(n):
            if land[i][j] == 1:
                # 석유가 있는 경우 탐색하기
                land[i][j] = cnt
                size = 1
                queue = deque()
                queue.append((i, j))
                while queue:
                    y, x = queue.popleft()
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0 <= ny < n and 0 <= nx < m and land[ny][nx] == 1:
                            land[ny][nx] = cnt
                            queue.append((ny, nx))
                            size += 1
                oil_size[cnt] = size
                cnt += 1
    
    # set으로 열에 있는 석유크기가 중복되지 않게 카운팅
    for j in range(m):
        total = set()
        for i in range(n):
            if land[i][j] >= 2:
                total.add(land[i][j])
                
        # set에 저장된 석유 개수 세기
        oil_sum = 0
        # print(total)
        for t in total:
            oil_sum += oil_size[t]
        
        answer = max(oil_sum, answer)    
    # for i in range(n):
    #     for j in range(m):
    #         print(land[i][j],end=' ')
    #     print()
    # print(oil_size)
    return answer