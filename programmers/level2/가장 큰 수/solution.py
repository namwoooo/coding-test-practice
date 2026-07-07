from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y == y + x:
        return 0
    else:
        return 1
    
def solution(numbers):
    str_numbers = [str(x) for x in numbers]
    
    if sum(numbers) == 0:
        answer = '0'
    else:
        str_numbers = sorted(str_numbers, key=cmp_to_key(compare))
        answer = ''.join(str_numbers)
    
    return answer