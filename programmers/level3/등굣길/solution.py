def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]  # 가능한 경로의 수 저장
    
    for i in range (n):
        for j in range(m):
            if [j + 1, i + 1] in puddles:
                continue
                
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    answer = dp[n - 1][m - 1] % 1000000007
    return answer