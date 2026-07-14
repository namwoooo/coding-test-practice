from collections import deque 

def solution(bridge_length, weight, truck_weights):
    time = 1
    cur_weight = 0
    on_bridge = deque()
    
    while truck_weights:
        for w in truck_weights:
            while w in truck_weights:
                # 오랜된 아이 퇴출
                if on_bridge and time - on_bridge[0][1] == bridge_length:
                    on_bridge.popleft()
                    cur_weight -= on_bridge[0][0]

                # bridge 꽉 안 참 & weight가 다음 것까지 가능
                if len(on_bridge) > bridge_length and cur_weight + w <= weight:
                    on_bridge.append((w, time))
                    cur_weight += w
                    truck_weights.remove(w)
                    time += 1

                # bridge 꽉 참 || weight가 다음게 안 됨 
                else:
                    time += 1
    
    return time