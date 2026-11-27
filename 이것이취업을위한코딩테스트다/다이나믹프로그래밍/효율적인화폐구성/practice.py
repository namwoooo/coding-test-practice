n, m = map(int, input().split())
array = []
d = [0] * (m + 1)

# array = [2, 3, 4]
for i in range(n):
  array.append(int(input()))

for i in range(min(array), m + 1):
  for j in array:
    if i > j and d[i - j] != 0:
      if d[i] == 0:
        d[i] = d[i - j] + 1
      else:
        d[i] = min(d[i], d[i - j] + 1)
    elif i == j:
      d[i] = 1
  print(d[i])

print(d[m])
