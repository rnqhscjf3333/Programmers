#숫자의 표현
from collections import deque

def solution(n):
    answer = 0
    
    dq = deque()
    for i in range(1, n+1):
        dq.append(i)
        while(sum(dq)>n):
            dq.popleft()
        if(sum(dq)==n):
            answer+=1

    return answer