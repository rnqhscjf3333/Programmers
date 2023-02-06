def solution(ingredient):
    answer = 0
    i=3
    while(i<len(ingredient)):
        if(i>=3 and ingredient[i]==1 and ingredient[i-1]==3 and ingredient[i-2]==2 and ingredient[i-3]==1):
            del ingredient[i-3]
            del ingredient[i-3]
            del ingredient[i-3]
            del ingredient[i-3]
            answer+=1
            i-=3
        else:
            i+=1
        
    
    return answer