def solution(participant, completion):
    answer = ''
    tmp = 0
    dict = {}
    for i in participant:
        dict[hash(i)] = i
        tmp += hash(i)
    for i in completion:
        tmp -= hash(i)
    answer = dict[tmp]
    return answer