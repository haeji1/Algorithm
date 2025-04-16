def solution(diffs, times, limit):
    start = 1
    end = max(diffs)
    # answer의 초기값은 end로 두기
    answer = end
    
    while start <= end:
        # diffs[0] = 1 이므로 항상 첫번째 문제는 풀 수 있다
        time = times[0]
        mid = (start + end) // 2
        # mid 값으로 퍼즐 풀리는지 체크
        for i in range(1, len(diffs)):
            # 퍼즐 레벨이 더 높은 경우
            if diffs[i] > mid:
                wrong = diffs[i] - mid
                time += (times[i - 1] + times[i]) * wrong + times[i]
            # 퍼즐 레벨이 더 낮은 경우    
            else:
                time += times[i]
                
        # 모든 시도 후 시간이 limt를 초과하는지 체크
        # limits보다 작으므로 더 적은시간으로 시도
        if time <= limit:
            answer = mid
            end = mid - 1
        # 초과했으므로 숙련도 높이기
        else:
            start = mid + 1
            
    return answer