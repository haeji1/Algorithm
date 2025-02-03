n = int(input())
visited = [0] * n
# print(visited)

def recursive(idx, result):
    global visited
    
    # basis part
    if idx == n:
        print(*result)
        return
        
    # inductive part
    for i in range(0, n):
        if not visited[i]:
            visited[i] = 1
            result.append(i+1)
            recursive(idx + 1, result)
            visited[i] = 0
            result.pop()


recursive(0, [])