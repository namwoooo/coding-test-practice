
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)  # 최대 떡 길이 
result = 0

while start <= end:
  total = 0  # 잘린 떡 길이의 총합 

  mid = (start + end) // 2

  for x in array:
    if x > mid:
      total += x - mid 

  if total >= m:
    result = max(result, mid) 
    start = mid + 1
  else:
    end = mid - 1

print(result)
