#우박수열 정적분
def solution(k, ranges):
    answer = []
    
    ans = [k]
    
    while(k!=1):
        if k%2 ==0:
            k//=2
        else:
            k=k*3+1
        ans.append(k)
        
    print(ans)
    
    for i in ranges:
        a=i[0]
        b=len(ans)+i[1]-1
        
        sumt = 0
        
        if a>b:
            answer.append(-1)
        else:
            
            for t in range(a,b):
                sumt+=min(ans[t],ans[t+1])+abs(ans[t]-ans[t+1])/2
            answer.append(sumt)
    
    
    
    return answer