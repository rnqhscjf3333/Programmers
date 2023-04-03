#택배 상자
from collections import deque
def solution(order):
    answer = 0
    
    n = len(order)
    
    box = [i+1 for i in range(n)]
    box = deque(box)
    container = deque()
    
    for i in order:
        while len(box)>0 and box[0]<i:
            container.append(box.popleft())
            
        if len(box)>0 and box[0]==i:
            box.popleft()
            answer+=1
            continue
        elif len(container)>0 and container[-1]==i:
            container.pop()
            answer+=1
            continue
        else:
            break
        
    
    
    return answer