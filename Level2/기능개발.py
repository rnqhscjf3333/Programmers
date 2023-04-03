#기능개발
import math
def solution(progresses, speeds):
    answer = []
    ma = 0
    for i in range(len(progresses)):
        t=math.ceil((100-progresses[i])/speeds[i])
        if(t>ma):
            ma = t
            answer.append(1)
        else:
            answer[-1]+=1
    
    
    return answer