n, m = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()

res = []
def recursive(idx):
    # basis part
    if len(res) == m:
        print(*res)
        return

    # inductive part
    for i in range(idx, n):
        res.append(numbers[i])
        recursive(i)
        res.pop()

recursive(0)