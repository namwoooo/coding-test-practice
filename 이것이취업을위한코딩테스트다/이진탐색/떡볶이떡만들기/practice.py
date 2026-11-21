import time

def cut_ddeok():

  n, m = map(int, input().split())  # N, M
  ddeok = list(map(int, input().split()))  # 주어진 떡들

  t = time.time()

  # n개의 떡들을 모두 result만큼 잘랐을 때 총합이 m인 result의 최댓값 
  # ddeok을 sort -> 
  ddeok.sort()
  cut = 0
  cut_ddeok = [0] * n

  def avg(array):
    return sum(array) // len(array)

  def binary_search(array, idx, start, end, cut):
    if start >= end:
      return

    mid = avg(array[start : end])

    for i in range(n):
      cut_ddeok[i] = max(array[i] - m, 0)

    if sum(cut_ddeok) >= m:
      cut = max(cut, mid)
      binary_search(array, mid + 1, end, cut)
    else:
      binary_search(array, start, mid - 1, cut)

  binary_search(ddeok, 0, n - 1, cut)
  
  print(time.time() - t)
  print(cut)

cut_ddeok()