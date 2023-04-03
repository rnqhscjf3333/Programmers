#롤케이크 자르기
from collections import deque
def solution(topping):
    answer = 0
    
    n = len(topping)
    
    a=set()
    b = {}
    
    for i in topping:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
            
    for i in topping:
        a.add(i)
        b[i]-=1
        if b[i]==0:
            del b[i]
        if len(a)==len(b):
            answer+=1
    
    
    return answer