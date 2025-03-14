def solution(video_len, pos, op_start, op_end, commands):
    pos_mm, pos_ss = map(int,pos.split(":"))
    op_start_mm, op_start_ss = map(int,op_start.split(":"))
    op_end_mm, op_end_ss = map(int,op_end.split(":"))
    video_mm, video_ss = map(int,video_len.split(":"))
    
     # 시작할 때 오프닝 구간인 경우 고려
    if (op_start_mm < pos_mm == op_end_mm and pos_ss < op_end_ss) or \
        (op_start_mm < pos_mm < op_end_mm) or \
        (op_start_mm == pos_mm == op_end_mm and op_start_ss <= pos_ss <= op_end_ss) or \
        (op_start_mm == pos_mm < op_end_mm and op_start_ss <= pos_ss):
            pos_mm, pos_ss = op_end_mm, op_end_ss
    
    
    for c in commands:     
        # 1. prev
        if c == 'prev':
            if pos_ss - 10 < 0 and pos_mm > 0:
                pos_mm -= 1
                pos_ss = 60 + (pos_ss - 10)
            else:
                pos_ss = max(0, pos_ss - 10)
                
        # 2. next
        elif c == 'next':
            if pos_ss + 10 >= 60 and pos_mm < video_mm:
                pos_mm += 1
            if pos_mm == video_mm:
                pos_ss = min((pos_ss + 10) % 60, video_ss)
            else:
                pos_ss = (pos_ss + 10) % 60
 
        # 연산을 마친 후 오프닝 구간인 경우 고려
        if (op_start_mm < pos_mm == op_end_mm and pos_ss < op_end_ss) or \
        (op_start_mm < pos_mm < op_end_mm) or \
        (op_start_mm == pos_mm == op_end_mm and op_start_ss <= pos_ss <= op_end_ss) or \
        (op_start_mm == pos_mm < op_end_mm and op_start_ss <= pos_ss):
            pos_mm, pos_ss = op_end_mm, op_end_ss

    return str(pos_mm).zfill(2) + ":"+str(pos_ss).zfill(2)