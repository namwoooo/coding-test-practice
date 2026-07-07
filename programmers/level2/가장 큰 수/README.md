## 가장 큰 수 lv2

링크: https://school.programmers.co.kr/learn/courses/30/lessons/42746 <br />
풀이 시간: 40분 / 30분

**어려웠던 점**
앞자리 수가 같고 뒷 자리 수들을 비교해야 하는 부분에서 어려움이 있었다.

itertools의 permutations를 사용해 각 조합을 모두 생성하여 int로 바꾼 값들 중 가장 큰 수를 선택하는 방식을 적용했다.
구현 결과 정답이 도출되기는 하지만 타임 아웃으로 오답 처리가 되었다.

## 오답 노트
#### 1차 오답(7/7) - 20분 (힌트 참고)

**핵심 아이디어**
sorted 함수에는 key(조건)를 지정하여 그에 따라 정렬할 수 있다.
이번에는 cmp_to_key를 활용해서 y + x가 x + y보다 클 경우 1을 반환하여 둘의 위치를 바꾸는 방식으로 문제를 해결했다.

**더 나은 방법**
map 함수로 리스트의 각 요소를 str 함수를 적용하고, sorted의 key로 lambda 함수로 x * 3이 큰 순서대로 정렬하는 방식을 사용할 수 있다.
이때 3을 곱하는 이유는 전제 조건에서 1000이하의 자연수라고 하였기 때문에 2를 곱하면 그래도 겹치는 일이 생겨 3을 곱하고 만약 10000이하라면 4를 곱하는 방식을 취할 수 있다.

```python
def solution(numbers):
  numbers = list(map(str, numbers))  # numbers 요소들에 대해 str 적용 후 list 변환
  numbers.sorted(key = lambda x: x*3, reverse = true)  # 조건에 맞게 내림차순 정렬 

  return str(int(''.join(numbers)))  # 0000 같은 경우에는 0으로만 출력해야 돼서 int로 변환 후 다시 str로 변환⭐
```