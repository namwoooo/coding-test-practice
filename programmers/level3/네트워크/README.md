## 네트워크 lv3

링크: https://school.programmers.co.kr/learn/courses/30/lessons/43162 <br />
풀이 시간: 1시간

**어려웠던 점** 
- queue를 사용하여 구현을 하긴 했지만 네트워크가 노드 한 개로만 이루어진 경우 네트워크 수 + 1이 되지 않아 문제가 생겼다
-> q에 초기값으로 첫 번째 노드를 준 상태로 while문 진입 & answer + 1을 while 문 끝에서 수행하지 말고 q를 빈 상태로 while문에 넣고 q가 비어있을 경우 조건문을 맨 위에 달아 count를 제일 먼저 해준다.