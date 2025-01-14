def recursive(idx, cnt, result, length, arr):
    # basis part
    if cnt == 6:
        print(*result)
        return

    # inductive part
    for i in range(idx, length - 1):
        result[cnt] = arr[i]
        recursive(i + 1, cnt + 1, result, length, arr)

while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    else:
        result = [0] * 6
        recursive(0, 0, result, len(arr), arr[1:])
        print()

