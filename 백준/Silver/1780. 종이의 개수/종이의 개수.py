n = int(input())
graph = [[] * n for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().split()))

result = {-1:0, 0:0, 1:0}
# 모두 같은 종이인지 확인
def is_same_value(y, x, size):
    number = graph[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if graph[i][j] != number:
                return False
    return True


# 9등분으로 나누기
def divide_and_conquer(y, x, size):
    if is_same_value(y, x, size):
        result[graph[y][x]] += 1
        return

    size //=  3
    for i in range(3):
        for j in range(3):
            divide_and_conquer(y + i * size, x + j * size, size)

divide_and_conquer(0, 0, n)

for i in result:
    print(result[i])
