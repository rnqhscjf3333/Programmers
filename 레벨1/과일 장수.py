def solution(k, m, score):
    score.sort(reverse = True)
    answer = 0
    answer1 = 0
    count = 0
    
    i=0
    while(i<len(score)):
        if(i+m<=len(score)):
            answer+=m*score[i+m-1]
        i+=m
            
    return answer