#큰 수 만들기
import sys
sys.setrecursionlimit(10**5)
answer = 0
ans = []
def solution(number, k):
    
    i=0
    while(i<len(number)-1 and k>0):
        if(number[i]<number[i+1]):
            number = number[:i]+number[i+1:]
            i = max(-1,i-2)
            k-=1
        i+=1
    for i in range(k):
        number = number[:-1]
        
    return number