#무인도 여행


import sys
sys.setrecursionlimit(10**5)
maps = []
a1 = 0
b1 = 0
def solution(map1):
    global maps
    global a1
    global b1
    maps = map1
    
    a1 = len(maps)-1
    b1 = len(maps[0])-1


    answer = []
    a = 0
    b = 0
    for a in range(a1+1):
        for b in range(b1+1):
            if(maps[a][b] != "X"):
                answer.append(sol(a,b))
                
    answer.sort()
    if(len(answer)==0):
        return [-1]
    return answer

def sol(a, b):
    global maps
    global a1
    global b1
    
    if(maps[a][b]=="X"):
        return 0
    
    c = int(maps[a][b])
    
    
    maps[a] = maps[a][:b]+"X"+maps[a][b+1:]
    
    c+=sol(min(a1,a+1),b)
    c+=sol(max(0,a-1),b)
    c+=sol(a,min(b1,b+1))
    c+=sol(a,max(0,b-1))
    
    return c