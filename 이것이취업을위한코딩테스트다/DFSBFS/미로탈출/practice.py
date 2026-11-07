from collections import deque

def escape_maze():

  n, m = map(int, input().split())  # N x M
  graph = []
  counts = []
  queue = deque()

  for i in range(n):
    graph.append(list(map(int, input())))

  print(graph)
  # count = 1  # 방문한 칸 수 

  def bfs(x, y, count):
    if x < 0 or y < 0 or x > n or y > m:
      return False

    # 탈출구면 True 반환
    if (x == n - 1) and (y == m - 1):
      counts.append(count)
      return True

    if graph[x][y] == 1:
      graph[x][y] = 0
      bfs(x - 1, y, count + 1)
      bfs(x + 1, y, count + 1)
      bfs(x, y - 1, count + 1)
      bfs(x, y + 1, count + 1)

    return False

  print(min(counts))

escape_maze()
    

