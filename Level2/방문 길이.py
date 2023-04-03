#방문 길이
def solution(dirs):
    answer = 0
    loc = [0,0]
    loc2 = []
    
    for i in dirs:
        if(i=="U"):
            loc1 = [loc[0],loc[1]+1]
        elif(i=="D"):
            loc1 = [loc[0],loc[1]-1]
        elif(i=="R"):
            loc1 = [loc[0]+1,loc[1]]
        elif(i=="L"):
            loc1 = [loc[0]-1,loc[1]]
        if(abs(loc1[0])>5 or abs(loc1[1])>5):
            continue
            
        if([loc, loc1] not in loc2 and [loc1, loc] not in loc2):
            loc2.append([loc,loc1])
            answer+=1
        loc = loc1
            
    #print(loc)
    return answer