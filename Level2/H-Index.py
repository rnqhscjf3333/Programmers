#H-Index
def solution(citations):
    answer = 0
    
    t = max(citations)
    
    while(t>answer):
        if(citations.count(t)>0):
            citations.remove(t)
            answer+=1
        else:
            t-=1
    
    return answer