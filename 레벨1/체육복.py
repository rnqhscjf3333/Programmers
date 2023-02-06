#체육복
def solution(n, lost, reserve):
    ans = []
    answer=0
    
    for i in range(n):
        if (i+1) in lost and (i+1) in reserve:
            ans.append(1)
        elif (i+1) in lost:
            ans.append(0)
        elif (i+1) in reserve:
            ans.append(2)
        else:
            ans.append(1)
    
    for i in range(n):
        if(ans[i]==0):
            if(i!=0 and ans[i-1] ==2):
                ans[i-1]=1
                ans[i]=1
            elif(i!=n-1 and ans[i+1] ==2):
                ans[i+1]=1
                ans[i]=1
        if(ans[i]>0):
            answer+=1
        
    return answer