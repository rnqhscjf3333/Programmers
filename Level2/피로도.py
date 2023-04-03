#피로도
answer = 0
def solution(k, dungeons):
    n = len(dungeons)
    
    def sol(nk, nd, nt):
        global answer
        
        for i in range(len(nd)):
            if nd[i][0]<=nk and nd[i][1]<=nk:
                sol(nk-nd[i][1], nd[:i]+nd[i+1:], nt+1)
        answer = max(answer, nt)
            
        
        
    sol(k, dungeons.copy(), 0)
    
    
    
    
    return answer
