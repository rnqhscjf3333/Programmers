#다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = [0 for i in range(bridge_length)]
    
    while(truck_weights != []):
        answer+=1
        del bridge[0]
        if(sum(bridge)+truck_weights[0]<=weight):
            bridge.append(truck_weights[0])
            del truck_weights[0]
        else:
            bridge.append(0)
        #print(bridge)
            
    
    
    return answer+bridge_length