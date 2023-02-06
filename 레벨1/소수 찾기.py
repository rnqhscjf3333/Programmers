#소수 찾기

def solution(n):
    answer = 0
    ans = [0 for i in range(n+1)]
    
    for i in range(1,n):
        if(ans[i+1]==1):
            continue
        elif is_prime_number(i+1):
            answer+=1
        for i in range(0,n+1,i+1):
            ans[i]=1
    
    return answer

def is_prime_number(x):#소수
    i=2
    while(i*i<=x):
        if x % i == 0:
            return False
        i+=1
    return True 