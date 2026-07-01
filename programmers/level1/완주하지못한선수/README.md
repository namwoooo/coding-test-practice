## 완주하지 못한 선수 lv1

링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576
풀이 시간: 10분

#### 막혔던 부분
- dict_keys type을 어떻게 원하는 문자열만 빼서 string으로 저장할 것인가
    - Counter.keys() → dict_keys([’leo’])
    
    📍 1. **join 함수 사용**
    
    ```python
    keys = dict_keys([’leo’])
    
    answer = ‘, ‘.join(keys)
    ```
    
    📍 2. **list 변환 (더 좋은 방법)**
    
    ```python
    keys = dict_keys(['leo'])
    answer = list(keys)[0]
    ```