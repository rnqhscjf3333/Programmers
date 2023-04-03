#튜플
def solution(s):
    answer=[]
    ans = [[] for i in range(10000)]
    
    a=1
    for i in range(1,len(s)-1):
        if(s[i]=="{"):
            a=i+1
        if(s[i]=="}"):
            st = s[a:i].split(",")
            ans[len(st)]= st
    
    
    i=1
    while(ans[i]!=[]):
        for t in ans[i]:
            if t not in ans[i-1]:
                answer.append(int(t))
                break
        i+=1
    
    
    #print(ans)
    return answer