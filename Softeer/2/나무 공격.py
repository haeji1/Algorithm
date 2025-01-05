n, m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

l1, r1 = map(int,input().split())
l2, r2 = map(int,input().split())

def simulation(y, x):
    global m
    for i in range(y, x):
        for j in range(m):
            if array[i][j] == 1:
                array[i][j] = 0
                break

simulation(l1 -1, r1)
simulation(l2 -1, r2)

result = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            result += 1

print(result)