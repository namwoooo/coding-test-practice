def solution(numbers, target):
    # 각 요소를 이어 트리라고 생각해보기 (0 -> (1, -1) -> (1, -1) ...)
    
    # numbers = [1, 1, 1, 1, 1]  root: 0, target: 3
    answer = 0  # 도달 가능한 방법 수
    
    def dfs(idx, total):
        nonlocal answer
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        dfs(idx + 1, total + numbers[idx])
        dfs(idx + 1, total - numbers[idx])
    
    dfs(0, 0)
    
    return answer