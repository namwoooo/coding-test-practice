def solution(progresses, speeds):
    
    days = []  # 배포까지 남은 일수
    answer = []  # 기능 개수
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            print(progresses[i])
            days.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            days.append((100 - progresses[i]) // speeds[i])
    
    count = 1
    current = days[0]  # 현재 일수
    
    for k in range(1, len(days)):
        if days[k] <= current:
            count += 1
        else:
            answer.append(count)
            count = 1
            current = days[k]
    
    answer.append(count)
            
    return answer