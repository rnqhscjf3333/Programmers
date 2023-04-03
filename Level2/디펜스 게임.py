#디펜스 게임
from collections import deque
from heapq import heappop
from heapq import heappush

def solution(n, k, enemy):
    answer = 0
    dq = deque(enemy)
    
    ans = []
    sumt = 0
    
    while k>=0 and len(dq)>0:
        dl = dq.popleft()
        
        
        
        sumt+=dl
        
        if sumt>n and k==0:
            break
        
        heappush(ans, (-1)*dl)
        
        if sumt>n:
            sumt+=heappop(ans)
            k-=1
            answer+=1

    return answer+len(ans)