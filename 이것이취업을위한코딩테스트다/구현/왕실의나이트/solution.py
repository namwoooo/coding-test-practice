import time

def night():
  input_data = input()

  t = time.time()

  # 각각의 변수에 좌표를 담음
  row = int(input_data[1])
  col = int(ord(input_data[0]) - ord('a')) + 1

  # 움직일 수 있는 경우
  steps = [(-2, 1), (2, 1), (-2, -1), (2, -1), 
          (1, 2), (1, -2), (-1, 2), (-1, -2)]

  result = 0 
  for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row > 0 and next_col > 0 and next_row < 9 and next_col < 9:
      result += 1

  print(time.time() - t)
  return result

result = night()
print(result)
