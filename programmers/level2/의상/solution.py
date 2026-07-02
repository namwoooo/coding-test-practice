from collections import Counter

def solution(clothes):
    
    answer = 1
    clothes_type = []
    
    for i in range(len(clothes)):
        clothes_type.append(clothes[i][1])
    clothes_counter = Counter(clothes_type)
    
    for k in range(len(clothes_counter)):
        answer = answer * (list(clothes_counter.values())[k] + 1)
        
    return answer - 1