import time

def sort_desc():
  n = int(input())  # 총 개수
  array = []

  for i in range(n):
    array.append(int(input()))

  t = time.time()

  count = [0] * (max(array) + 1)

  for i in range(len(array)):
    count[array[i]] += 1

  for i in range(len(count) - 1, 0, -1):
    for j in range(count[i]):
      print(i, end=' ')

  print(time.time() - t)

sort_desc()
