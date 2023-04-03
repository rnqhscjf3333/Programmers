#2 x n 타일링
#파보나치수열
import sys
sys.setrecursionlimit(10**5)
t= []
def solution(n):
    answer = 0
    
    count1 = 1
    count2 = 2
    
    if(n==1):
        return count1
    elif(n==2):
        return count2
    else:
        for i in range(n-2):
            temp = count2
            count2 = count1+count2
            count1 = temp
        return count2%1000000007