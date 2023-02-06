def solution(number):
    answer = 0
    
    for i in range(len(number)-2):
        for u in range(i+1, len(number)-1):
            for t in range(u+1, len(number)):
                if(number[i]+number[u]+number[t]==0):
                    answer+=1
    
    return answer