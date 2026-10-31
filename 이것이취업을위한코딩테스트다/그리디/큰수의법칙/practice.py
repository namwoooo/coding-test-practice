def big_number_rule():

  # n: 배열의 크기, m: 더해지는 숫자 개수, k: 연속 더하기 제한 횟수
  inputs = input().split(' ')
  n, m, k = int(inputs[0]), int(inputs[1]), int(inputs[2])
  arr = [int(x) for x in input().split(' ')]

  sum = 0
  sequence = 0

  # arr 내림차순 정렬
  arr.sort(reverse=True)

  # 첫 번째랑 두 번째 값만 더하면 됨 
  for i in range(m):
    if sequence != 0 and sequence % k == 0:
      sum += arr[1]
      sequence += 1
      continue
    sum += arr[0]
    sequence += 1

  return sum

result = big_number_rule()
print(result)