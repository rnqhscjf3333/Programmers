#캐시
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    dq = deque()
    
    if(cacheSize==0):
        return len(cities)*5
    
    for i in cities:
        i = i.lower()
        if i not in dq:
            answer+=5
            if len(dq)< cacheSize:
                dq.append(i)
            else:
                dq.popleft()
                dq.append(i)
        else:
            answer+=1
            dq.remove(i)
            dq.append(i)
        #print(dq)
    
    
    
    return answer