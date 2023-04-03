#줄 서는 방법
def solution(n, k):
    ans = [i+1 for i in range(n)]
    answer=[]
    fact = [1]
    k-=1

    
    for i in range(1,n+1):
        fact.append(i*fact[i-1])
        
    for i in range(n-1,0,-1):
        answer.append(ans[k//fact[i]])
        del ans[k//fact[i]]
        k-=(k//fact[i])*fact[i]
        
        
        
    answer.append(ans[k//fact[i]])
    
    
    return answer