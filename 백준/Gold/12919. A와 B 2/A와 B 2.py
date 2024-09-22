s = input()
t = input()
length = len(s)
res = 0

# t -> s
def make_t(result):
    global res
    # 종료조건
    if result == s:
        res = 1
        return

    if len(result) < length:
        return

    # A 없애기
    if result[-1] == 'A':
        make_t(result[:-1])

    # 뒤집고 B 없애기
    if result[0] == 'B':
        make_t(result[1:][::-1])


make_t(t)
print(res)

