n = int(input())
top = list(map(int,input().split()))
stack = []
result = [0] * n

for i in range(n):
    # stack의 최상단 원소 값이 더 큰지 확인
    while stack and top[stack[-1]] <= top[i]:
        stack.pop()
    # stack이면 더 큰 값의 인덱스가 저장되어있으므로 result에 할당
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(*result)
