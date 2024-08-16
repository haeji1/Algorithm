def solution(s):
    answer = True
    stack = []
    for ss in s:
        if ss == '(':
            stack.append('(')
        elif ss == ')':
            if not stack:
                answer = False
                return answer
            else:
                stack.pop()
    if stack:
        answer = False
    return answer