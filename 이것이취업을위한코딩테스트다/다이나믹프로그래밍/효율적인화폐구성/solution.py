n, m = map(int, input().split())
array = []

for _ in range(n):
  array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for i in range(1, m + 1):
  for j in array:
    if i >= j:
      d[i] = min(d[i], d[i - j] + 1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
