n = int(input())
array = list(map(int,input().split()))
stack = []
result = [-1] * n

for i in range(n):
    # stack에 들어있는 값 -> 오큰수를 구하고자 하는 인덱스
    # array[i] -> 오큰수인지 현재 탐색하는 값
    while stack and array[stack[-1]] < array[i]:
        # array[i]가 오큰수라면 pop
        result[stack.pop()] = array[i]
    stack.append(i)
print(*result)