from collections import deque 

def solution(n, computers):
    # computers[i]: 각 컴퓨터, computers[i][j]: 각 컴퓨터와 연결된 컴퓨터 
    # visited에서 모두 나갈 때까지 체크 
    
    visited = set(range(len(computers))) 
    q = deque()
    answer = 0
    
    while visited: 
        if not q:
            answer += 1
            q.append(min(visited))
            visited.remove(min(visited))
            
        current = q.popleft()
        for i in range(len(computers)):
            if computers[current][i] == 1 and i in visited:
                q.append(i)
                visited.remove(i)
    
    return answer