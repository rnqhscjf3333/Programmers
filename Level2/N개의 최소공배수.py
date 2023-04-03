#N개의 최소공배수
def solution(arr):
    answer = 0
    
    arr.sort(reverse=True)
    
    a = arr[0]
    for i in arr:
        t=1
        while((a*t)%i!=0):
            t+=1
        a*=t
        
    
    
    return a