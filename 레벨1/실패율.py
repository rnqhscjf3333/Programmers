#실패율
def solution(N, stages):
    answer = []
    ans1 = [0 for i in range(N+1)]#도전수
    ans2 = [0 for i in range(N+1)]#성공수
    
    ans = {}
    
    for i in stages:
        for t in range(i):
            ans1[t]+=1
        ans2[i-1]+=1
        

    
    for i in range(N):
        if(ans1[i]==0):
            ans[i+1]=0
        else:
            ans[i+1] = ans2[i]/ans1[i]
        
    
    sorted_dict = sorted(ans.items(), key = lambda item: item[1], reverse = True)
    
    
    for i in sorted_dict:
        answer.append(i[0])
    
    return answer