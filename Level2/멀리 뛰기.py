#멀리 뛰기
#런타임 에러 ; 재귀함수 횟수
dp = [0 for i in range(2001)]
def solution(n):
    
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    
    return dp[n]%1234567 