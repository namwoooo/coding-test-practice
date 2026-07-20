## 정수 삼각형 lv3

링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105 <br />
풀이 시간: 16분

**어려웠던 점** 
- dp[i][j]에 이전 값 + 현재 값을 할 때 이전 값을 triangle에서가 아닌 dp에서 가져와야 한다는 점을 놓쳤다.
- 최종 반환값을 max(dp[len(triangle) - 1])을 해야 하는데 max(dp[len(triangle)])을 해서 out of index 에러가 발생했다.