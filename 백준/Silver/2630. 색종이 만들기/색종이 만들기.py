n = int(input())
graph = [[] * n for _ in range(n)]
result = {0:0, 1:0}

for i in range(n):
    graph[i] = list(map(int,input().split()))

# 같은 색인지 확인
def is_same_value(y,x,size):
    num = graph[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if graph[i][j] != num:
                return False
    return True

# 4등분 하기
def divide_and_conquer(y, x, size):
    if is_same_value(y,x,size):
        result[graph[y][x]] += 1
        return
    size //= 2
    for i in range(2):
        for j in range(2):
            divide_and_conquer(y + i * size, x + j * size, size)

divide_and_conquer(0,0,n)

for i in result:
    print(result[i])