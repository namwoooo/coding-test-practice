import time

def game_develop():
  n, m = map(int, input().split())  # N x M 
  row, col, direction = map(int, input().split()) # 현재 위치, 방향
  game_map = []

  for i in range(n):
    game_map.append(input().split())

  count = 1  # 총 방문한 칸의 수 
  rotation = 0
  visited = [[[0] for i in range(m)] for j in range(n)]

  t = time.time()

  # 가보거나 바다인 칸은 1
  # 뒤가 바다라서 못 움직이면 끝

  while True:
    # 왼쪽 방향에 안 가본 칸이 있다면, 왼쪽으로 회전해서 한 칸 전진 
    # 북쪽  
    if direction == 0 :
      if col - 1 >= 0 and game_map[row][col - 1] == 0 and visited[row][col - 1] == 0 and rotation + 1 != 4:
        count += 1
        col -= 1
        visited[row][col] == 1
        rotation += 1
        direction = 3
        continue
      elif rotation + 1 != 4:
        rotation += 1
        direction = 3
      else:
        if row - 1 >= 0 and game_map[row -1][col] == 0:
           row -= 1 
           continue
        else:
           break

    elif direction == 1 :
          if row + 1 < n and game_map[row + 1][col] == 0 and visited[row + 1][col] == 0 and rotation + 1 != 4:
            count += 1
            row += 1
            visited[row][col] == 1
            rotation += 1
            direction = 0
            continue
          elif rotation + 1 != 4:
            rotation += 1
            direction = 0
          else:
            if col - 1 >= 0 and game_map[row][col - 1] == 0:
              col -= 1 
              continue
            else:
                break

    elif direction == 2 :
          if col + 1 < m and game_map[row][col + 1] == 0 and visited[row][col + 1] == 0 and rotation + 1 != 4:
            count += 1
            col += 1
            visited[row][col] == 1
            rotation += 1
            direction = 1
            continue
          elif rotation + 1 != 4:
            rotation += 1
            direction = 1
          else:
            if row + 1 < n and game_map[row +1][col] == 0:
                row += 1 
                continue
            else:
                break

    elif direction == 3 :
              if row - 1 >= 0 and game_map[row - 1][col] == 0 and visited[row - 1][col] == 0 and rotation + 1 != 4:
                count += 1
                row -= 1
                visited[row][col] == 1
                rotation += 1
                direction = 2
                continue
              elif rotation + 1 != 4:
                rotation -= 1
                direction = 2
              else:
                if col + 1 < m and game_map[row][col + 1] == 0:
                    col += 1 
                    continue
                else:
                    break
    print(time.time() -t)
    return count

result = game_develop()
print(result)


    
