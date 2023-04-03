#짝지어 제거하기
from collections import deque

def solution(s):
    
    if(len(s)%2 !=0):
        return 0

    dq = deque()
    
    for i in s:
        if(len(dq)>0 and dq[-1]==i):
            dq.pop()
        else:
            dq.append(i)

    return 1 if len(dq)==0 else 0