#예상 대진표
import math
def solution(n,a,b):
    answer = 0
    
    
    while(True):
        if(a==b):
            return answer
        
        if(a>n/2 and b>n/2):
            a-=n/2
            b-=n/2
        
        if(a<=n/2 and b<=n/2):
            n/=2
            a=math.ceil(a/2)
            b=math.ceil(b/2)
        else:
            return int(math.log2(n))+answer
        answer+=1
        

    return answer