#n^2 배열 자르기
import math
def solution(n, left, right):
    answer = []
    
    t = left//n
    t1 = right//n
    
    for a in range(t,t1+1):
        for b in range(n):
            if a <= b:
                answer.append(b+1)
            else:
                answer.append(a+1)
    
    
    
    return answer[left-t*n:right-t*n+1]