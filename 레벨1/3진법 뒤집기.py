#3진법 뒤집기
def solution(n):
    answer = ""
    ans = 0
    
    i=1
    while(i*3<=n):
        i*=3
    t = 1
    while(i>0):
        if(n//i>0):
            ans+=n//i*t
            answer=str(n//i)+answer
            n%=i
        else:
            answer="0"+answer
        i//=3
        t*=3
    
    
    return ans