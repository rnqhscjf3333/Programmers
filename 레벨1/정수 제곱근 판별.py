#정수 제곱근 판별
import math
def solution(n):
    a = int(math.sqrt(n))

    if(a*a==n):
        return (a+1)*(a+1)
    else:
        return -1