#괄호 변환

def solution(p):
    answer = ''
    
    left = 0
    right = 0
    i=0
    ias = False
    
    while(i<len(p)):
        
        if(p[i]=="("):
            left+=1
        else:
            right+=1
            
        if(right>left):
            ias = True
        
        
        if(left==right):
            if(ias==False):
                answer+=p[:i+1]
                p = p[i+1:]
                i=-1
            else:
                answer+=sol(p[:i+1], p[i+1:])
                #print(p[:i+1], p[i+1:])
                return answer
                
        i+=1
        
    return answer



                
        

def sol(a,b):
    c = "("+solution(b)+")"
    newa = ""
    for i in range(1,len(a)-1):
        if(a[i]=="("):
            newa+=")"
        else:
            newa+="("
    
    
    return c+newa