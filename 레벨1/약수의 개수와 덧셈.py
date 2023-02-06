#약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        t=0
        count=0
        while(t*t<=i):
            t+=1
            if(i%t==0):
                if(t*t==i):
                    count+=1
                else:
                    count+=2
        if(count%2==0):
            answer+=i
        else:
            answer-=i
            
        
    
    return answer