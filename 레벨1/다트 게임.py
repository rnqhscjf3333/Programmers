#다트 게임
def solution(dartResult):
    answer = 0
    
    a = 0 #현재원래점수
    b = 0 #현재점수
    c = 0 #이전점수
    i=0
    while(i<len(dartResult)):
        if(dartResult[i]=="S"):
            answer+=a
            b = a
        elif(dartResult[i]=="D"):
            answer+=a**2
            b = a**2
        elif(dartResult[i]=="T"):
            answer+=a**3
            b = a**3
        elif(dartResult[i]=="#"):
            answer-=b*2
            b = (-1)*b
        elif(dartResult[i]=="*"):
            answer+=b
            answer+=c
            b *=2
            
        else:
            c = b
            if(i<len(dartResult)-1 and dartResult[i]=="1" and dartResult[i+1] == "0"):
                a = 10
                i+=1
            else:
                a = int(dartResult[i])
        i+=1
        #print(a, b, c, answer)
    
    
    
    return answer