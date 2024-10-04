h, w = map(int,input().split())
blocks = list(map(int,input().split()))

result = 0
for i in range(1, w - 1):
    left = max(blocks[:i])
    right = max(blocks[i + 1:])
    now = blocks[i]
    if left > now and right > now:
        result += min(left, right) - now

print(result)