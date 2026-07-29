import heapq

def solution(scoville, K):
    answer = 0  # 섞은 횟수
    heap = []   # scoville heap
    
    for s in scoville:
        heapq.heappush(heap, s)  # 전부 넣기 -> [1,2,3,9,10,12]
    
    while not all(s >= K for s in scoville):
        if len(heap) >= 2:
            new_scoville = heapq.heappop(heap) + heapq.heappop(heap) * 2
            heapq.heappush(heap, new_scoville)
            answer += 1
        else: 
            return -1
    
    return answer