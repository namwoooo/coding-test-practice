## 폰켓몬 lv1

링크: https://school.programmers.co.kr/learn/courses/30/lessons/1845 <br />
풀이 시간: 5분

**더 간결하게 쓰는 법**

📍 Counter를 꼭 사용할 필요 없이 set으로도 충분히 가능함! 

꼭 개수를 센다고 Counter를 사용할 필요가 없다

```python
# 가져갈 폰켓몬 수가 작으면 그만큼, 종류가 더 작으면 종류 수만큼만 가져갈 수 있음 

def solution(nums):
	return min(len(nums)/2, len(set(nums)))
```