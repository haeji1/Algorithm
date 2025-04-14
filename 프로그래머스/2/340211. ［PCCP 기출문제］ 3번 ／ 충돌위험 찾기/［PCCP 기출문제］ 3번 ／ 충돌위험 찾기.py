from collections import defaultdict, Counter
def solution(points, routes):
    answer = 0
    path = defaultdict(list)
    
    # 시작위치 확인
    for route in routes:
        time = 0
        y, x = points[route[0] - 1][0], points[route[0] - 1][1]

        # 타겟위치가 여러 곳인 경우 고려해서 확인
        for i in range(1, len(route)):
            target_y, target_x = points[route[i] - 1][0], points[route[i] - 1][1]
            
            # 가장 첫 좌표 저장
            if i == 1:
                path[time].append((y, x))
            
            # y좌표 선 이동
            while y != target_y:
                if y < target_y:
                    y += 1
                else:
                    y -= 1
                time += 1
                path[time].append((y,x))
                
            # x좌표 이동
            while x != target_x:
                if x < target_x:
                    x += 1
                else:
                    x -= 1
                time += 1
                path[time].append((y, x))
                
    
    for p in path:
        c = Counter(path[p])
        for key in c:
            if c[key] > 1:
                answer += 1
                
    return answer