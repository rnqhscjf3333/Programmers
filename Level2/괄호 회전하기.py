#괄호 회전하기
from collections import deque

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        #print(s)
        dq = deque()
        
        st = True
        for t in s:
            if(t=="[" or t=="(" or t=="{"):
                dq.append(t)
            else:
                if(not dq):
                    st = False
                    break
                d = dq.pop()
                
                if(t=="]" and d  != "["):
                    st = False
                    break
                if(t==")" and d  != "("):
                    st = False
                    break
                if(t=="}" and d  != "{"):
                    st = False
                    break
        if(st == True and not dq):
            answer+=1
        
        s = s[1:]+s[0]

    return answer