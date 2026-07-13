def solution(n, times):
    left, right = 0, max(times) * n   # 가능한 시간대의 총 범위
    mid = (left + right) // 2
    answer = right
    
    while left <= right:
        mid = (left + right) // 2 
        
        people = sum([mid // t for t in times])
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer