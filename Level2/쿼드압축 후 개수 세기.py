#쿼드압축 후 개수 세기
def solution(arr):
    answer = [0,0]
    n=len(arr)
    
    
    def sol(ar):
        
        n = len(ar[0])
        if(n<=1):
            if(ar[0]==[1]):
                answer[1]+=1
            else:
                answer[0]+=1
        else:
            a,b,c,d=[],[],[],[]
            nt = n//2
            

            for i in range(nt):
                a.append(ar[i][:nt])

            for i in range(nt):
                b.append(ar[i][nt:])

            for i in range(nt,n):
                c.append(ar[i][:nt])

            for i in range(nt,n):
                d.append(ar[i][nt:])
                
            for i in (a,b,c,d):
                su=0
                for t in i:
                    su+=sum(t)
                if(su==0):
                    answer[0]+=1
                elif(su==nt*nt):
                    answer[1]+=1
                else:
                    sol(i)
                
    su=0
    for i in arr:
        su+=sum(i)
    if(su==0):
        return [1,0]
    if(su==n*n):
        return [0,1]
    
    
    sol(arr)
    
    return answer