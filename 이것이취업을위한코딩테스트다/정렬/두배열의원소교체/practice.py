import time

def make_sum_max():

  n, k = map(int, input().split())  # N, K

  array_A = list(map(int, input().split()))
  array_B = list(map(int, input().split()))

  t = time.time()

  # 최대 k번 바꿔치기 가능 
  # A의 모든 요소가 B의 모든 요소보다 큼 
  # 둘 다 정렬하고 시작
  array_A.sort()
  array_B.sort(reverse=True)
  count = 0


  for i in range(n):
    if array_A[i] < array_B[i]:  # B의 원소가 더 큰 경우에만 switch
      array_A[i], array_B[i] = array_B[i], array_A[i]
      count += 1

    if count == k:
      break

  print(time.time() - t)
  return sum(array_A)

    

result = make_sum_max()
print(result)