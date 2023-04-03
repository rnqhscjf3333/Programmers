#점 찍기
def solution(k, d):
    answer = 0
    
    x = d
    
    for y in range(d+1):
        if y%k==0:
            while x**2+y**2>d**2:
                x-=1
            answer+=x//k+1
    
    
    
    
    return answer