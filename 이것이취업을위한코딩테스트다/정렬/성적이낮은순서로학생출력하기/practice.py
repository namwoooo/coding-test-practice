import time

def sort_low_score():
  n = int(input())   # 입력 수
  student = {}       # 학생 정보 입력받는 dict
  scores = []

  for i in range(n):
    name, score = input().split()
    student[int(score)] = name
    scores.append(int(score))

  t = time.time()

  scores.sort()

  for s in scores:
    print(student[s], end=' ')

  print(time.time() - t)

sort_low_score()
