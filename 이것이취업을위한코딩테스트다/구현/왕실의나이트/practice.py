import time

def night():
  curr = input()  
  curr = list(curr) # ['a', '1']
  total = 0  # 이동할 수 있는 가짓수

  t = time.time()

  # 좌2위1, 좌2아래1, 우2위1, 우2아래1, 위2좌1, 위2우1, 아래2좌1, 아래2우1
  
  # 좌
  if curr[0] >= 'c':
      if int(curr[1]) >= 2 and int(curr[1]) <= 7:
         total += 2
      elif int(curr[1]) >=2 or int(curr[1]) <= 7:
         total += 1

  # 우
  if curr[0] <= 'f':
        if int(curr[1]) >= 2 and int(curr[1]) <= 7:
           total += 2
        elif int(curr[1]) >=2 or int(curr[1]) <= 7:
           total += 1

  # 위
  if int(curr[1]) >= 3:
      if curr[0] >= 'b' and curr[0] <= 'g':
        total += 2
      elif curr[0] >= 'b' or curr[0] <= 'g':
        total += 1

  # 아래
  if int(curr[1]) <= 6:
        if curr[0] >= 'b' and curr[0] <= 'g':
          total += 2
        elif curr[0] >= 'b' or curr[0] <= 'g':
          total += 1

  print(time.time() - t)
  return total

result = night()
print(result)

  