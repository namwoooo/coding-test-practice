def solution(arr):
    answer = -1
    dp, minus, plus = [], [], []
    
    if "-"  not in arr:
        answer = sum([arr[x] for x in range(0, len(arr), 2)])
    
    dp.append([int(arr[0])])
    
    for i in range(1, arr, 2):
        if arr[i] == "-":
            minus.append(i)
        elif arr[i] == "+":
            plus.append(i)
    
    answer = answer + arr[:]
    
    return answer