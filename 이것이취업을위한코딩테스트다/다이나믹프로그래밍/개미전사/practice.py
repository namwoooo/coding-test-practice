n = int(input())  # 창고 수
array = list(map(int, input().split()))

count = [0] * (n + 1)
count[0] = array[0]
count[1] = array[1]
count[2] = array[0] + array[2]

if n == 3:
  print(max(count[n - 1], count[n - 2]))
else:
  for i in range(3, n):
    count[i] = array[i] + max(count[i - 2], count[i - 3])

  print(max(count[n - 1], count[n - 2]))

