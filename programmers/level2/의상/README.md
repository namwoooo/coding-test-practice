## 의상 lv2

링크: https://school.programmers.co.kr/learn/courses/30/lessons/42578 <br />
풀이 시간:28분

**어려웠던 점**
- clothes[i][1]을 Counter에 넣었을 때 알파벳으로 분리되어 count 됨
  -> '문자열'이 Counter에 들어가기 때문에 알파벳으로 분리된다. <br />

  **해결**: Counter에 바로 넣지 않고 다른 list에 종류만 모은 후 Counter에 입력

📍 Counter를 꼭 사용할 필요 없이 dictionary를 사용할 수도 있다

어차피 리스트로 새로 만들 것이라면 dictionary로 생성해서 'type: count' 로 묶을 수 있다.

```python
def solution(clothes):

  clothes_dict = {}

  for c, t in clothes:
    if t not in clothes_dict:
      clothes_dict[t] = 2       # 장식 수 1 + 아무것도 입지 않을 경우
    else:
      clothes_dict[t] += 1      # 장식 수 + 1

  answer = 1
  for n in clothes_dict.values():
    answer *= n
  
	return answer - 1
```