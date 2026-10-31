import time

def until_one():
  n, k = map(int, input().split())

  t = time.time()
  count = 0
  # 최소 횟수가 되는 방법 
  # k가 n의 약수라면 -> k가 1만 아니면 더 빠름 k가 1이라면 n-1이 정답 

  while True:
    if n == 1:
      print(time.time() - t)
      return count
  
    if n % k == 0:
      n //= k
      count += 1
    else:
      n -= 1
      count += 1

result = until_one()
print(result)