#카펫
def solution(brown, yellow):
    answer = []
    
    br = brown//2
    br+=2
    
    a=2
    while(a<=br//2):
        b=br-a
        print(a,b)
        if(a*b==brown+yellow):
            return b,a
        a+=1
    
    
    
    return a