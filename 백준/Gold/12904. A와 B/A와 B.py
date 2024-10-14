s = input()
t = input()
def make_s(t):
    while len(t) > len(s):
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] == 'B':
            t = t[:-1]
            t = t[::-1]

    # s로 만들 수 있는지 확인
    if t == s:
        return 1
    else:
        return 0
print(make_s(t))