def solution(n):
    
    i=2
    while(i*i<n):
        if((n-1)%i==0):
            return i
        i+=1
    return n-1