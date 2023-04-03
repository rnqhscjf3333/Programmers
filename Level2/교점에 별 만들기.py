#교점에 별 만들기
def solution(line):
    answer = []
    ans = set()
    
    minx = 1000000000000000
    maxx = -1000000000000000
    miny = 1000000000000000
    maxy = -1000000000000000
    
    
    
    for a in range(len(line)-1):
        for b in range(a+1, len(line)):
            cd = sol(line[a],line[b])
            if(cd != False):
                ans.add(cd)
                minx = min(cd[0],minx)
                maxx = max(cd[0],maxx)
                miny = min(cd[1],miny)
                maxy = max(cd[1],maxy)
                
    #print(ans)
    #print(minx,maxx,miny,maxy)
    
    for y in range(maxy,miny-1,-1):
        ast = ""
        for x in range(minx,maxx+1):
            if((x,y) in ans):
                ast += "*"
            else:
                ast += "."
        answer.append(ast)
        
    
    
    
    return answer

def sol(line1, line2):
    A = line1[0]
    B = line1[1]
    E = line1[2]
    C = line2[0]
    D = line2[1]
    F = line2[2]
    
    if(A*D-B*C==0):
        return False
    
    x = (B*F-E*D)/(A*D-B*C)
    y = (E*C-A*F)/(A*D-B*C)
    if(x!=int(x) or y != int(y)):
        return False
    
    return int(x),int(y)