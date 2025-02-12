n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

result = 1e9

# 인원 나누기 위한 방문 배열
visited = [0] * n

def recursive(idx, cnt):
    global result
    # basis part
    if cnt == n // 2:
        start_team = 0
        link_team = 0
        # 모두 방문한 팀 -> start팀, 방문하지 않은 팀 -> link팀
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start_team += array[i][j]
                elif not visited[i] and not visited[j]:
                    link_team += array[i][j]

        # 차이의 최솟값 갱신
        result = min(result, abs(start_team - link_team))

    # inductive part
    # 인원이 n//2로 나뉘지 않았을 때 계속 나누기
    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = 1
                recursive(i + 1, cnt + 1)
                visited[i] = 0

recursive(0, 0)
print(result)
