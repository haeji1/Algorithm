t = int(input())
for tc in range(t):
    bomb = []
    result = 0
    n = int(input())
    for _ in range(2):
        bomb.append(input())

    # 확정된 지뢰 '*' 더하기
    for i in range(n):
        if bomb[1][i] == '*':
            result += 1

    # 각 자리에 있을 수 있는 지뢰 수 탐색
    for i in range(n):
        if '0' < bomb[0][i] <= '9':
            tmp = int(bomb[0][i])
        else:
            continue

        # 확정된 지뢰가 있다면 탐색 해야할 지뢰 수 -1
        for j in (1, 0, -1):
            y = 1
            x = i + j

            # 더 이상 탐색 해야할 지뢰가 없다면 탐색 종료
            if tmp == 0:
                break

            if 0 <= x < n and bomb[y][x] == '*':
                tmp -= 1

        # 확정되지 않은 지뢰 탐색
        for j in (1, 0, -1):
            y = 1
            x = i + j

            if tmp == 0:
                break

            # 확정된 지뢰 배열 내부에서 수정
            if 0 <= x < n and bomb[y][x] == '#':
                bomb[1] = bomb[1][:x] + '*' + bomb[1][x + 1:]
                result += 1
                tmp -= 1

    print(result)
