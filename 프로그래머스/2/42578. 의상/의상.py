def solution(clothes):
    dict_clothes = {}
    answer = 1
    for i in range(len(clothes)):
        if clothes[i][1] not in dict_clothes:
            dict_clothes[clothes[i][1]] = [clothes[i][0]]
        else:
            dict_clothes[clothes[i][1]].append(clothes[i][0])
    
    # 조합 구하기 -> 카테고리 내 아무것도 선택하지 않는 경우 + 1
    for category in dict_clothes:
        answer *= (len(dict_clothes[category]) + 1)
        
    # 아무것도 선택하지 않는 경우 제외
    answer -= 1
  
    return answer