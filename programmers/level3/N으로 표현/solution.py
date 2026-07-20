def solution(N, number):
    
    dp = [set() for _ in range(9)]  # 값을 저장할 리스트
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N, NN, NNN 추가
        
        for j in range(1, i + 1):   # 이전 값들 간의 사칙연산 수행 
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        
        if number in dp[i]:
            return i
        
    return -1