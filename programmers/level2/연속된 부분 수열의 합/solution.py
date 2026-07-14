def solution(sequence, k):
    left = 0
    window_sum = 0
    min_len = float('inf')
    answer = []
    
    for right in range(len(sequence)):
        window_sum += sequence[right]
        while window_sum >= k:
            if window_sum == k:
                if min_len > right - left + 1:
                    min_len = right - left + 1
                    answer = [left, right]
            window_sum -= sequence[left]
            left += 1
                
    return answer