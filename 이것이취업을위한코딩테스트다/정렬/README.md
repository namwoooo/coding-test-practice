## 정렬

일반적으로 문제에서 요구하는 **조건**에 따라 적절한 정렬 알고리즘을 사용하도록 해야 한다.
<br/>

### 정렬의 종류

- 선택 정렬
- 삽입 정렬
- 퀵 정렬
- 계수 정렬

<br/>

### 선택 정렬

**가장 작은 데이터를 선택**해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하는 방식이다.
<br/>
<br/>
    
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        min_index = i   # 가장 작은 원소의 인덱스 

        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        
        array[i], array[min_index] = array[min_index], array[i]  # 스와프
    print(array)
    
<br/>

- **시간 복잡도**: O(N<sup>2</sup>)
- 기본 정렬 라이브러리(`sort()`)나 퀵 정렬과 비교했을 때 매우 비효율적
- 하지만, 특정한 리스트에서 **가장 작은 데이터를 찾는 일**에 자주 사용된다.
<br/>
<br/>

### 삽입정렬

모든 데이터를 순환하며 각 데이터를 **적절한 위치에 삽입**시키는 방식이다.
<br/>

선택 정렬에 비해 시간 측면에서 더 효율적이고, 필요할 때만 위치를 바꾸기 때문에 **'데이터가 거의 정렬되어 있을 때'** 훨씬 효율적이다.
<br/>
<br/>

삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 **이미 정렬되어 있다고 가정**한다. 그래서 시작을 두 번째 데이터부터 한다. 

<br/>
<br/>

    
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(1, len(array)):
      for j in range(i, 0 , -1):
        if array[j]  < array[j - 1]:
          array[j], array[j - 1] = array[j - 1], array[j]
        else:
          break
    print(array)
    
<br/>
      
- **시간 복잡도**: 최선 -> O(N), 최악 -> O(N<sup>2</sup>)
- 현재 리스트가 거의 정렬되어 있다면 매우 빠르게 동작한다.
  - 거의 정렬되어 있으면 퀵 정렬보다도 좋은 선택이 될 수 있다.


### 퀵 정렬

퀵 정렬은 정렬 알고리즘 중 가장 많이 사용되는 알고리즘 중 하나이다. <br/> 
퀵 정렬과 병합 정렬은 대부분의 프로그래밍 언어에서 정렬 라이브러리의 근간이 되는 알고리즘이기도 한 빠른 알고리즘들이다.
<br/>
<br/>

퀵 정렬은 **기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는** 방식으로 구현된다.
<br/>
<br/>

이때 기준 데이터로 **pivot**을 사용하는데, pivot을 설정하고 리스트를 분할하는 방법에 따라 여러 가지 방법으로 퀵 정렬을 구분한다.
<br/>
<br/>

가장 대표적인 분할 방식은 **호어 분할**이다.

- 리스트에서 첫 번째 데이터를 pivot으로 정한다.
- 왼쪽에서부터 pivot보다 큰 데이터를 찾고, 오른쪽에서부터 pivot보다 작은 데이터를 찾아 큰 데이터와 작은 데이터의 위치를 서로 교환한다. (첫 번째로 찾은 수를 선택)
- 찾는 값의 위치가 서로 엇갈릴 때까지 반복하며, 엇갈리면 반복을 멈추고 pivot을 그 사이에 넣는다.
- 그러면 pivot을 중심으로 왼쪽은 pivot보다 작은 값만, 오른쪽은 pivot보다 큰 값만 모여 있다.
- 이 작업을 리스트의 개수가 한 개일 때까지 반복한다.

<br/>
<br/>

    ```python
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort(array, start, end):
      if start >= end:  # 원소가 1개인 경우
        return
      
      pivot = start
      left = start + 1
      right = end

      while left <= right:
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] >= array[pivot]:
          left += 1
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] =< array[pivot]:
          right -= 1
        
        # 엇갈렸으면 pivot이랑 작은 값(array[right])랑 바꾸기
        if left > right:
          array[pivot], array[right] = array[right], array[pivot]
        else: 
          array[left], array[right] = array[right], array[left]

      # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
      quick_sort(array, start, right - 1)
      quick_sort(array, right + 1, end)

    quick_sort(array, 0, len(array) - 1)
    print(array)
    ```

<br/>
<br/>

- **시간 복잡도**: O(NlogN) (최악은 O(N<sup>2</sup>))

<br/>
<br/>

### 계수 정렬
계수 정렬은 **데이터의 크기가 0이상이고, 최솟값과 최댓값의 차이가 100만을 넘지 않을 경우**에 효과적으로 상요할 수 있다. <br/>
(데이터의 크기가 제한되어 있을 때에 한해서 데이터의 개수가 매우 많더라도 빠르게 동작한다.)
<br/>
<br/>

- 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성한다. 리스트의 **인덱스**가 데이터의 범위를 포함할 수 있어야 한다.
- 처음에는 리스트의 모든 데이터를 0으로 초기화한다.
- 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.
- 전체를 기록하고 난 후, 리스트의 첫 번째 데이터부터 하나씩 그 값만큼 **인덱스를 출력**한다.

<br/>
<br/>

```python
# 모든 원소의 값이 0보다 크거나 같다고 가정 
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
  for j in range(count[i]):
    print(i, end=' ')  # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력 
```

<br/>
<br/>

- **시간 복잡도**: O(N + K)
- **공간 복잡도**: 경우에 따라 심각한 비효율성을 초래할 수 있다. (예: 데이터가 0과 999,999)
<br/>
<br/>

### sorted()
파이썬이 제공하는 기본 정렬 라이브러리 `sorted()`는 일반적으로 퀵 정렬보다 느리지만, 최악의 경우에도 **O(NlogN)**을 보장한다는 특징이 있다.
<br/>
<br/>

- 딕셔너리, 집합 자료형 등을 입력받아도 **리스트**를 반환한다.
- 리스트 객체의 내장 함수인 `sort()`를 사용하면 별도의 정렬된 리스트가 아니라, 내부 원소가 바로 정렬된다.
- `sorted()`나 `sort()`에 key 매개변수를 입력받을 수 있다.
  - key 값으로는 하나의 함수가 들어가며, 해당 함수를 기준으로 정렬된다.

<br/>
<br/>

