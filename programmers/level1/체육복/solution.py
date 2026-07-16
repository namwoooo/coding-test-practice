def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    # lost = reserve 인 사람 제외
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = -1
    
    # 앞 또는 뒤의 사람한테 빌려주기 
    for i in range(len(reserve)):
        # 앞의 사람
        if reserve[i] - 1 in lost:
            lost.remove(reserve[i] - 1)
            reserve[i] = 0
            continue
        elif reserve[i] + 1 in lost:
            lost.remove(reserve[i] + 1)
            reserve[i] = 0
            continue
    
    lost = [x for x in lost if x != -1]
    
    return n - len(lost)