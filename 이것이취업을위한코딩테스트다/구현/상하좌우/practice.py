import time

def up_down_left_right():
  n = int(input())  # N x N 
  movement = input().split()  # 움직임
  curr = [1, 1]  # 현재 좌표 (초기화) 

  # R: 오른쪽, L: 왼쪽, U: 위, D: 아래
  # 시작은 (1, 1), 공간을 벗어나는 명령은 무시 
  t = time.time()
  for m in movement:
      if m == "R":
        if curr[1] < n:
          curr[1] += 1
      elif m == "L":
        if curr[1] > 1:
          curr[1] -= 1
      elif m == "U":
        if curr[0] > 1:
          curr[0] -= 1
      else:
        if curr[0] < n:
          curr[0] += 1

  print(time.time() - t)
  return curr
  


result = up_down_left_right()
print(f"{result[0]} {result[1]}")

