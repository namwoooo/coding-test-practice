## 기능개발 lv2

링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586 <br />
풀이 시간: 30분 / 40분

**어려웠던 점** 
각 기능들의 배포까지 남은 일수를 계산하는 작업까지는 진행했지만 어떻게 해야 
배포되는 날마다의 새롭게 배포되는 기능 수가 몇 개인지 기록할 수 있는지에 대해 고민됐다.
그래서 이틀의 고민 끝에 일단 답안 코드를 참고해보기로 했다

```python
def solution(progresses, speeds):
  ####  남은 일수 기록 리스트 days ####

  count = 1   # 배포되는 새로운 기능 수를 기록하는 변수
  current = days[0]    # 배포되는 날 기록

  for k in range (len(days)):
    if days[k] <= current:  # 현재 배포되는 날보다 작은 경우
      count += 1
    else:
      answer.append(count)
      count = 1           # count 초기화
      current = days[k]   # current 변경
  
  answer.append(count)    # 마지막 count 더해주기

  return answer
```