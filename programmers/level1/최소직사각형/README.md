## 최소직사각형 lv1

링크: https://school.programmers.co.kr/learn/courses/30/lessons/86491 <br />
풀이 시간: 30분

**해결 방법** 
commands에 요구된 범위만큼 슬라이싱하고 퀵 정렬을 구현하여 정렬 후 요구되는 값 선택

**더 나은 방법**
더 단순하게 sorted 함수를 사용할 수 있다.

```python
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```