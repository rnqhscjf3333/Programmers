#N-Queen
#백트래킹

answer = 0
def solution(n):
    global answer
    for i in range(n):
        sol([],i,n)
        
    return answer

def sol(col,i,n):
    global answer
    
    isk = False
    
    b = len(col)
    
    for a in range(len(col)):
        if(col[a]==i or abs(b-a) == abs(i-col[a])):
            isk = True
            break
            

    if(isk == False):
        if(len(col)==n-1):
            #print(col+[i])
            answer+=1
        else:  
            for a in range(n):
                if(a != i):
                    sol(col+[i],a,n)