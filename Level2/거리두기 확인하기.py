#거리두기 확인하기
def solution(places):
    answer = []
    
 
    def sol1(place):
        pl = []
        for x in range(5):
            for y in range(5):
                if(place[x][y]=="P"):
                    pl.append([x,y])
        print(pl)
        for x in range(len(pl)-1):
            for y in range(x+1,len(pl)):
                ab = abs(pl[x][0]-pl[y][0])+abs(pl[x][1]-pl[y][1])
                if ab==1:
                    return 0
                if ab==2:
                    print(pl[x],pl[y])
                    if abs(pl[x][0]-pl[y][0])==2 or abs(pl[x][1]-pl[y][1])==2:
                        if place[(pl[x][0]+pl[y][0])//2][(pl[x][1]+pl[y][1])//2]=="O":
                            return 0
                    else:
                        if place[pl[x][0]][pl[y][1]] == "O" or place[pl[y][0]][pl[x][1]] == "O":
                            return 0


                    
        return 1
        
    for i in range(len(places)):
        answer.append(sol1(places[i]))

    
    return answer