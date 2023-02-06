def solution(k, score):
    answer = []
    nscore = []
    for i in score:
        nscore.append(i)
        nscore.sort(reverse = True)
        
        answer.append(nscore[min(len(nscore), k)-1])
    
    
    return answer