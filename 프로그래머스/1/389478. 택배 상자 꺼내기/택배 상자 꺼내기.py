def solution(n, w, num):
    answer = 0
    height = 0
    # 세로 크기 구하기
    if n % w == 0:
        height = n // w
    else:
        height = n // w + 1
    
    ware_house = [[0] * w for _ in range(height)]
    
    # 상자 넣기
    box = 1
    for i in range(height):
        for j in range(w):
            if box > n:
                break
            ware_house[i][j] = box
            box += 1
                
    for i in range(height):
        if i % 2 != 0:
            ware_house[i].reverse()
            
    for i in range(height):
        for j in range(w):
            if ware_house[i][j] == num:
                if ware_house[height - 1][j] != 0:
                    answer = height - i
                else:
                    answer = height - i - 1
        
    print(ware_house)
    return answer