## 게임 맵 최단거리 lv2

링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844 <br />
풀이 시간: 30분 / 41분

**어려웠던 점** 
- 최단 거리를 구할 때는 BFS를 떠올려야 한다
- queue를 어떻게 구성할지 -> (x, y, dist)
- 상하좌우를 탐색하는데 각각의 조건을 다르게 할 것 (상, 좌는 각 row, col이 0 이상이도록 / 하, 우는 각 row, col이 n, m 미만이도록 설정)