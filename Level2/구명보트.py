#구명보트
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    
    dq = deque(people)
    
    while dq:
        if(len(dq)==1):
            answer+=1
            break
        
        if(dq[0]+dq[-1]<=limit):
            dq.pop()
            dq.popleft()
        else:
            dq.pop()
        answer+=1
        
    
    return answer