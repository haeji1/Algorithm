def recursive(idx, cnt, result, arr):
    # basis part
    if cnt == 6:
        print(*result)
        return

    # inductive part
    for i in range(idx, len(arr)):
        result[cnt] = arr[i]
        recursive(i + 1, cnt + 1, result, arr)

while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    else:
        result = [0] * 6
        recursive(0, 0, result, arr[1:])
        print()

