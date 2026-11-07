from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

# 최단 거리를 찾아야 하기 때문에 bfs 사용
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  q = deque()
  q.append((x, y))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        q.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1  # 현재까지 총 방문한 칸 수 저장 

  return graph[n - 1][m - 1]

result = bfs(0, 0)
print(result) 