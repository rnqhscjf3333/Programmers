#영어 끝말잇기
from collections import deque
def solution(n, words):
    dq = deque()
    for i in words:
        if(i in dq):
            return [len(dq)%n+1, len(dq)//n+1]
        if(len(dq)>0 and i[0]!=dq[-1][-1]):
            return [len(dq)%n+1, len(dq)//n+1]
        dq.append(i)

   

    return [0,0]