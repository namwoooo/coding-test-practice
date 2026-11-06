def ice_cream():
  
  n, m = map(int, input().split())  # N x M
  count = 0   # 아이스크림의 총 개수 
  graph, visited = [], []

  for i in range(n):
    graph.append(input().split())
  
  visited = graph
  
  def rotation(graph, i, j, visited):
    # 0인 경우
    if graph[i][j] == 0:
      visited[i][j] = 1
      if i + 1 < n:
        rotation(graph, i + 1, j, visited) 
      if j + 1 < m:
        rotation(graph, i, j + 1, visited)
    # 1인 경우
    else:
      return 

  for i in range(n):
    for j in range(m):
      if visited[i][j] == 0:
        rotation(graph, i, j, visited)
        count += 1
      else:
        continue
  print(count)
  

ice_cream()
