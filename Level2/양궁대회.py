#양궁대회
#높은점수가 0이라고 무조건 1주면 안됨
answer = []
maxn = 0

def solution(n, info):
    global maxn
    
    
    def sol(n, Rinfo):
        global answer
        global maxn
        t = len(Rinfo)
        
        
        if n>0 and t<10:
            sol(n,Rinfo+[0])
            if info[t]<n:
                sol(n-info[t]-1, Rinfo+[info[t]+1])
        else:
            if n>0:
                Rinfo+=[n]
                t+=1
            mat = 0
            for i in range(10):
                if i<t and Rinfo[i]>0:
                    mat+=10-i
                elif info[i]>0:
                    mat-=10-i
            if mat>maxn:
                maxn = mat
                answer = Rinfo+[0]*(10-t+1)
            elif mat == maxn and answer != []:
                Rinfo = Rinfo+[0]*(10-t+1)
                for i in range(10,-1,-1):
                    if answer[i]>Rinfo[i]:
                        break
                    elif answer[i]<Rinfo[i]:
                        answer = Rinfo
                        break
    
    sol(n,[])
    
    if maxn == 0:
        return [-1]
    
    
    
    return answer