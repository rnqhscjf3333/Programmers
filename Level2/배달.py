#배달
def solution(N, road, K):
    answer = 0
    maps = [0,0]+[1000000]*(N-1)
    
    def sol(r):
        for i in road:
            if(i[0]==r[0] and maps[i[1]]>r[1]+i[2]):
                maps[i[1]]=r[1]+i[2]
                sol([i[1],r[1]+i[2]])
            elif(i[1]==r[0] and maps[i[0]]>r[1]+i[2]):
                maps[i[0]]=r[1]+i[2]
                sol([i[0],r[1]+i[2]])
        
            
    
    
    
    i=0
    for i in road:
        if(i[0]==1 and maps[i[1]]>i[2]):
            maps[i[1]] = i[2]
            sol(i[1:])
        elif(i[1]==1 and maps[i[0]]>i[2]):
            maps[i[0]] = i[2]
            sol([i[0],i[2]])
    
    i = 1
    while(i<=N):
        if(maps[i]<=K):
            answer+=1
        i+=1
    #print(maps)
    return answer