n = int(input())
array = list(map(int,input().split()))
array.sort()
max_number = -999
for i in range(2, array[-1] + 1):
    number = i
    cnt = 0
    for j in range(n):
        if array[j] % number == 0:
            cnt += 1
    if max_number < cnt:
        max_number = cnt

print(max_number)