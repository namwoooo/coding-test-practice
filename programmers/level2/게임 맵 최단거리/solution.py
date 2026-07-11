from collections import deque 

def solution(maps):
    # answer: 최단 거리 
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * m for _ in range(n)]  # 방문 기록  n x m
    q = deque([(0, 0, 1)])  # 초기화(시작점)
    
    while q:
        current = q.popleft()  # 현재 위치
        x, y, dist = current[0], current[1], current[2]
        
        if y - 1 >= 0 and maps[x][y - 1] != 0 and visited[x][y-1] == 0:
            visited[x][y - 1] = 1
            q.append((x, y - 1, dist + 1))
        if y + 1 < m and maps[x][y + 1] != 0 and visited[x][y + 1] == 0:
            visited[x][y + 1] = 1
            q.append((x, y + 1, dist + 1))
        if x - 1 >= 0 and maps[x - 1][y] != 0 and visited[x - 1][y] == 0:
            visited[x - 1][y] = 1
            q.append((x - 1, y, dist + 1))
        if x + 1 < n and maps[x + 1][y] != 0 and visited[x + 1][y] == 0:
            visited[x + 1][y] = 1
            q.append((x + 1, y, dist + 1))
            
        if x == n - 1 and y == m - 1:
            return dist
    return -1   # queue가 비었는데 목표 지점에 도달하지 못했을 경우