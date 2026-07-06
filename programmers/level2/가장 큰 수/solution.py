from itertools import permutations

def solution(numbers):
    
    answer = '0'
    answer_list = []
    
    for p in permutations(numbers, len(numbers)):
        answer_list.append(p)
    
    for l in range(len(answer_list)):
        current = ''.join(map(str, answer_list[l]))
        if int(current) > int(answer):
            answer = current
        
    return answer