#약수의 합
def solution(n):
    answer = 0
    
    i = 1
    while(i*i<=n):
        if(n % i==0):
            answer+=i
            if(i*i != n):
                answer+=n/i
        i+=1
    
    
    return answer