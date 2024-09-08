n, r, c = map(int,input().split())
size = 2 ** n
number = 0

def divide_and_conquer(y,x,size):
    global number

    # 종료 조건
    if y == r and x == c:
        print(number)
        exit(0)

    if size == 1:
        number += 1
        return

    # 벗어난 범위 체크 x
    if not (y <= r < y + size and x <= c < x + size):
        number += size * size
        return

    # 4등분
    size //= 2
    # Z로 채우는 재귀 호출
    divide_and_conquer(y, x, size)
    divide_and_conquer(y,  x + size, size)
    divide_and_conquer(y + size, x, size)
    divide_and_conquer(y + size, x + size, size)

divide_and_conquer(0,0,size)