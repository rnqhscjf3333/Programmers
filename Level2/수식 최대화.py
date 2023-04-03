#수식 최대화
answer = 0
def solution(expression):
    ans = []
    
    at = ""
    for i in expression:
        if(i.isdigit() == False):
            ans.append(int(at))
            ans.append(i)
            at = ""
        else:
            at+=i
    ans.append(int(at))
    
    def sol(ans, exp):
        global answer
        if(exp==[]):
            answer = max(answer,abs(ans[0]))
        else:
            for i in exp:
                t = 1
                anst = ans[:]
                while(t<len(ans)):
                    if(ans[t]==i):
                        if(i=="*"):
                            ans[t] = ans[t-1]*ans[t+1]
                            del ans[t+1]
                            del ans[t-1]
                        elif(i=="+"):
                            ans[t] = ans[t-1]+ans[t+1]
                            del ans[t+1]
                            del ans[t-1]
                        elif(i=="-"):
                            ans[t] = ans[t-1]-ans[t+1]
                            del ans[t+1]
                            del ans[t-1]
                    else:
                        t+=2
                exp2 = exp[:]
                exp2.remove(i)
                sol(ans, exp2)
                ans = anst
                
            
        
        
    sol(ans, ["-","+","*"])
    
    
    
    return answer