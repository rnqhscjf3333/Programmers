#올바른 괄호
#시간 초과
#스택 사용
from collections import deque

def solution(s):
    answer = True
    
    if(len(s)%2 != 0):
        return False
    
    dq = deque()
    for i in s:
        if(i=="("):
            dq.appendleft(i)
        else:
            if(not dq or dq.pop() != "("):
                return False
    if(dq):
        return False

    return True