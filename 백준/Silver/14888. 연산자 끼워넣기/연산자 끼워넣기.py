n = int(input())
numbers = list(map(int,input().split()))
calc = list(map(int,input().split()))
max_val = float('-inf')
min_val = float('inf')

def recursive(idx, value, c_sum, c_sub, c_mul, c_div):
    global max_val, min_val

    # basis part
    if idx == n:
        # 최댓값 갱신
        if max_val < value:
            max_val = value
        # 최솟값 갱신
        if min_val > value:
            min_val = value
        return

    # inductive part
    if c_sum < calc[0]:
        recursive(idx + 1, value + numbers[idx], c_sum + 1, c_sub, c_mul, c_div)
    if c_sub < calc[1]:
        recursive(idx + 1, value - numbers[idx], c_sum, c_sub + 1, c_mul, c_div)
    if c_mul < calc[2]:
        recursive(idx + 1, value * numbers[idx], c_sum, c_sub, c_mul + 1, c_div)
    if c_div < calc[3]:
        if value < 0:
            recursive(idx + 1, -(abs(value) // numbers[idx]), c_sum, c_sub, c_mul, c_div + 1)
        else:
            recursive(idx + 1, value // numbers[idx], c_sum, c_sub, c_mul, c_div + 1)

recursive(1,numbers[0],0,0,0,0)
print(max_val)
print(min_val)