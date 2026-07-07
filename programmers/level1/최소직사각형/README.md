## 최소직사각형 lv1

링크: https://school.programmers.co.kr/learn/courses/30/lessons/86491 <br />
풀이 시간: 30분

## 오답 노트
#### 1차 오답(7/7) - 3분 (힌트 참고)

**핵심 아이디어**
비교하기 전에 주어진 리스트에서 큰 값을 width, 작은 값을 height로 설정해두면 for문에서 중첩 조건문으로 모든 case를 확인할 필요가 없다.

**더 나은 방법**
큰 값들 중에서 가장 큰 값과 작은 값들 중에서 가장 큰 값의 곱으로 나타낼 수 있다.

```python
def solution(sizes):
  return max(max(x) for x in sizes) * max(min(x) for x in sizes)
```