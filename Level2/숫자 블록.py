#숫자 블록
import math 
def solution(begin, end):
    answer = []

    
    for i in range(begin, end+1):
        a=False
        if(i==1):
            answer.append(0)
            a=True
        else:
            for t in range(2, int(math.sqrt(i))+1):
                if(i%t==0 and i / t <= 10000000):
                    answer.append(i//t)
                    a=True
                    break
        if(a==False):
            answer.append(1)
                
        
    
    
    
    return answer