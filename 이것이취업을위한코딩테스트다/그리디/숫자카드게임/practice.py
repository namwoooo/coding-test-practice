def card_game():
  n, m = map(int, input().split())
  arr = []
  card = []  # 각 열의 min값 저장

  # n열만큼 입력받음 -> arr = [[], [], ...]
  for i in range(n):
    arr.append(list(map(int, input().split())))
    card.append(min(arr[-1]))

  # 각 줄마다 min을 뽑아 그 중에 가장 큰 거 선택
  return max(card)


result = card_game()
print(result)
