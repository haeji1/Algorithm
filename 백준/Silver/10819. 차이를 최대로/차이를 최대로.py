n = int(input())
array = list(map(int,input().split()))
calc = []
visited = [0] * n
max_value = float('-inf')
def recursive(idx):
    global max_value
    # basis part
    if idx == n:
        value = 0
        # 연산 실행
        for i in range(n - 1):
            value += abs(array[calc[i]] - array[calc[i + 1]])
        max_value = max(max_value, value)
        return

    # inductive part
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            calc.append(i)
            recursive(idx + 1)
            visited[i] = 0
            calc.pop()

recursive(0)
print(max_value)