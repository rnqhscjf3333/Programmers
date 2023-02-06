def solution(babbling):
    ba = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for i in range(len(babbling)):
        for t in range(4):
            if(babbling[i].find(ba[t])>=0):
                babbling[i] = babbling[i].replace(ba[t], str(t))
        answer+=1
        for u in range(len(babbling[i])):
            if(babbling[i][u] == '0' or babbling[i][u] == '1' or babbling[i][u] == '2' or babbling[i][u] == '3'):
                if(u==0):
                    continue
                elif(babbling[i][u-1]==babbling[i][u]):
                    answer-=1
                    break
            else:
                answer-=1
                break
                    
    #print(babbling)
    return answer