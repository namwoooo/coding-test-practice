def solution(sizes):
    # 핵심 아이디어: 미리 큰 값을 가로, 작은 값을 세로로 설정해두면 그것만 비교하면 됨
    max_w, max_h = 0, 0
    
    for l in sizes:
        c_w, c_h = max(l), min(l)  # 큰 값을 w, 작은 값을 h로 설정
        if c_w > max_w:
            max_w = c_w
        if c_h > max_h:
            max_h = c_h
        
    answer = max_w * max_h
    
    return answer