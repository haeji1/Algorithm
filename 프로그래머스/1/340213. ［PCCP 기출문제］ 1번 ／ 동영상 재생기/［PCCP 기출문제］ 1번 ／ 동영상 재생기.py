def solution(video_len, pos, op_start, op_end, commands):
    pos_mm, pos_ss = map(int,pos.split(":"))
    op_start_mm, op_start_ss = map(int,op_start.split(":"))
    op_end_mm, op_end_ss = map(int,op_end.split(":"))
    video_mm, video_ss = map(int,video_len.split(":"))
    
     # 시작할 때 오프닝 구간인 경우 고려
    if (op_start_mm < pos_mm < op_end_mm or
        op_start_mm != op_end_mm and op_start_mm == pos_mm and pos_ss >= op_start_ss or
        op_start_mm == pos_mm == op_end_mm and op_start_ss <= pos_ss < op_end_ss or
        op_start_mm != op_end_mm and pos_mm == op_end_mm and pos_ss < op_end_ss):
            pos_mm = op_end_mm
            pos_ss = op_end_ss
    
    print(pos_mm, pos_ss)
    for c in commands:    
        # 1. prev
        if c == 'prev':
            if pos_ss - 10 < 0 and pos_mm > 0:
                pos_mm -= 1
                pos_ss = (pos_ss + 60) - 10
            else:
                pos_ss = max(0, pos_ss - 10)
                
        # 2. next
        elif c == 'next':
            pos_ss += 10
            if pos_ss >= 60:
                pos_ss -= 60
                pos_mm += 1
                
            if pos_mm > video_mm:
                pos_mm = video_mm
                pos_ss = video_ss
            
            if pos_mm == video_mm and pos_ss > video_ss:
                pos_ss = video_ss
                
        if (op_start_mm < pos_mm < op_end_mm or
        op_start_mm != op_end_mm and op_start_mm == pos_mm and pos_ss >= op_start_ss or
        op_start_mm == pos_mm == op_end_mm and op_start_ss <= pos_ss < op_end_ss or
        op_start_mm != op_end_mm and pos_mm == op_end_mm and pos_ss < op_end_ss):
            pos_mm = op_end_mm
            pos_ss = op_end_ss
            
    pos_mm = str(pos_mm)
    pos_ss = str(pos_ss)
    pos_mm = pos_mm.zfill(2)
    pos_ss = pos_ss.zfill(2)
    answer = pos_mm +":"+ pos_ss
    return answer