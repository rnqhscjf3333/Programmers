#문자열 압축
def solution(s):
    answer = 100000000000000
    
    for i in range(1,max(len(s)//2+1,2)):
        t=0
        ans = 0
        pret = ""
        isa = 1
        
        while(t<len(s)):
            if(pret != s[t:t+i]):
                pret = s[t:t+i]
                ans+=len(s[t:t+i])
                isa = 1
            else:
                if(isa==1 or isa==9 or isa==99 or isa==999):
                    ans+=1
                isa+=1
            t+=i
        #print(i, ans)
        answer = min(answer,ans)
            
    
    
    return answer