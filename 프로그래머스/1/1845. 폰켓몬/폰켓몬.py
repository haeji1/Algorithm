def solution(nums):
    dict = {}
    cnt = 0
    answer = 0
    length = len(nums)
    num = length // 2
    
    # 폰켓몬 종류 세기
    for i in range(length):
        # 해당 키 없다면 초기화
        if nums[i] not in dict:
            dict[nums[i]] = 0
            cnt += 1
        dict[nums[i]] += 1
    
    # 폰켓몬 종류에 따라 종류 개수 출력
    if cnt > num:
        answer = num
    else:
        answer = cnt
    return answer