def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
        
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

def solution(array, commands):
    
    answer = []
    
    for i in range(len(commands)):
        sliced = array[commands[i][0] - 1:commands[i][1]]
        result = quick_sort(sliced)
        
        answer.append(result[commands[i][2] - 1])
        
    return answer