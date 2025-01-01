a = input()
length = len(a)
if length >= 10:
    cnt = 0
    for i in range(length // 10):
        for j in range(10):
            print(a[cnt],end='')
            cnt += 1
        print()
    print(a[cnt:])
else:
    print(a)