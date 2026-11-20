import time

def find_items():

  n = int(input())
  n_items = list(map(int, input().split()))

  m = int(input())
  m_items = list(map(int, input().split()))

  result = []

  t = time.time()

  n_items.sort()   # 이진 탐색을 위해 정렬

  def binary_search(array, target, start, end):
    if start > end:
      return "no"

    mid = (start + end) // 2
    if array[mid] == target:
      return "yes"
    elif array[mid] < target:
      return binary_search(array, target, mid + 1, end)
    else:
      return binary_search(array, target, start, mid - 1)


  for i in m_items:
    result.append(binary_search(n_items, i, 0, n - 1))

  print(time.time() - t)

  for i in range(len(result)):
    print(result[i], end=" ")

find_items()

