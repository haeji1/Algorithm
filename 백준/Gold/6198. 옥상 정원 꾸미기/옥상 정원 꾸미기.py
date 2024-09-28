n = int(input())
stack = []
buildings = []
result = 0
for _ in range(n):
    buildings.append(int(input()))

cnt = 0
for i in range(n):
    while stack and buildings[stack[-1]] <= buildings[i]:
        stack.pop()
    stack.append(i)
    result += len(stack) - 1

print(result)
