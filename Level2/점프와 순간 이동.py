#점프와 순간 이동
def solution(n):
    answer = 0
    
    if(n==1):
        return 1
    
    while(n!=1):
        if(n%2!=0):
            answer+=1
        n=n//2
        
    if(n>0):
        return 1+answer
    return answer