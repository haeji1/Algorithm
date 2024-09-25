t = int(input())
for _ in range(t):
    n = int(input())
    flag = 0
    phone_book = []
    for _ in range(n):
        phone_book.append(input())
    set_phone_book = set(phone_book)
    for p in phone_book:
        for i in range(1, len(p)):
            if p[:i] in set_phone_book:
                flag = 1
                break
    if flag:
        print('NO')
    else:
        print('YES')
