word = str(input())
bomb = str(input())
bomb_len = len(bomb)

# stack에 문자열 넣으면서 bomb가 존재하는지 뒤에서부터 확인
stack = []
for i in range(len(word)):
    stack.append(word[i])
    # print(stack[-bomb_len:])
    if ''.join(stack[-bomb_len:]) == bomb:
        for j in range(bomb_len):
            stack.pop()
if not stack:
    print("FRULA")
else:
    print(''.join(stack))
