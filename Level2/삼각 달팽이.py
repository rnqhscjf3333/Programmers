#삼각 달팽이
#한쪽으로 밀고 반복 규칙 찾는게 중요
def solution(n):
    answer = []
    
    ans = []
    nt = 0
    
    for i in range(n):
        nt+=i+1
        ans.append([0]*(i+1))


    
    x=0
    
    i=1
    
    while(i<nt):
        for t in range(x*2, n-1-x):
            ans[t][x] = i
            i+=1

        for t in range(x,n-1-x*2):
            ans[n-x-1][t] = i
            i+=1
  
        for t in range(n-1-x,x*2,-1):
            ans[t][t-x] = i
            i+=1
        x+=1

    for i in range(len(ans)):
        if 0 in ans[i]:
            ans[i][ans[i].index(0)]=nt
        answer+=ans[i]
    

    
    

    return answer