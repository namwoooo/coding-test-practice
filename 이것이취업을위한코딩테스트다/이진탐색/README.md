## 이진 탐색

### 순차 탐색
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법 
<br/>
<br/>

순차 탐색은 리스트에 특정 값의 원소가 있는지 체크하거나, 특정한 값을 가지는 원소의 개수를 세는 `count()` 메서드에서도 내부에서 순차 탐색이 수행된다.
<br/>
<br/>

```python
def sequential_search(n, target, array):
  # 각 원소를 하나씩 확인
  for i in range(n):
    if array[i] == target:
      return i + 1  # 현재의 위치 반환 
```
<br/>
<br/>

### 이진 탐색
**배열 내부의 데이터가 정렬된 상태**에서만 사용이 가능하다. <br/>
이진 탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색한다.
<br/>
<br/>

- 이진 탐색에서 위치를 나타내는 변수 3개: 시작점, 끝점, 중간점 
<br/>

찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하여 리스트를 반씩 줄여나간다.
<br/>
<br/>

이진 탐색을 구현하는 방법은 두 가지가 있다.
1. 재귀 함수
2. 반복문 

```python
# 재귀 함수 구현 
def binary_search(array, target, start, end):
  if start > end:
    return None
  
  mid = (start + end) // 2

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)
```

<br/>
<br/>

```python
# 반복문 구현
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  
  return None
```

<br/>
<br/>

데이터의 탐색 범위가 2000만을 넘어가면 이진 탐색으로 문제를 접근해보는 것이 좋다. 
<br/>
<br/>

- **시간 복잡도**: O(logN)
<br/>
<br/>

### 트리 자료구조
트리 구조는 노드와 노드의 연결로 표현하며, 여기에서 노드는 정보의 단위로서 어떠한 정보를 가지고 있는 개체이다. 
<br/>
<br/>

### 이진 탐색 트리
이진 탐색 트리란 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조이다. 
<br/>

- 왼쪽 자식 노드들은 부모 노드보다 작다.
- 오른쪽 자식 노드들은 부모 노드보다 크다.
<br/>
<br/>

#### 이진 탐색 트리에서 데이터를 조회하는 과정
1. 이진 탐색은 루트 노드부터 방문한다. target보다 루트가 크면 왼쪽을, 작으면 오른쪽을 방문한다.
2. target 값을 찾을 때까지 반복한다. 
3. 만약 더 이상 자식 노드가 없는데 target과 일치하는 노드를 찾지 못했다면 해당 트리에 존재하지 않는 것이다. 

<br/>
<br/>

보통 이진 탐색 문제는 입력 데이터가 매우 많다.(1000만 개 이상, 탐색 범위는 1000억 이상)
<br/>
<br/>

이러한 경우 `input()`을 사용하면 입력 단계에서 시간 초과가 날 수 있다. <br/>
그래서 `sys` 라이브러리의 `readline()` 함수를 이용하면 시간 초과를 피할 수 있다.

<br/>
<br/>

```python 
import sys

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()  # rstrip은 엔터 기호 삭제시키기 위해 사용 

# 입력받은 문자열 그대로 출력
print(input_data)
```
