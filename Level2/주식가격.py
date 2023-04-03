#주식가격
#스택
#12321
def solution(prices):
    n=len(prices)
    answer = [0 for _ in range(n)]
    ans = []
    
    
    for i in range(n):
        while ans != [] and ans[-1][0]>prices[i]:
            a,b = ans.pop()
            
            answer[b] = i-b
        
        ans.append([prices[i],i])
        
        for a,b in ans:
            answer[b] = n-b-1
    
    
    return answer