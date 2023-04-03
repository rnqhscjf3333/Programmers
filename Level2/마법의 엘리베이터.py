#마법의 엘리베이터
#반례 : 95, 555
def solution(storey):
    answer = 0
    
    sto = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(str(storey))):
        sto[i] = int(str(storey)[-(i+1)])
    
    for i in range(len(sto)):
        if(sto[i]==10):
            sto[i]=0
            sto[i+1]+=1
        if(sto[i]<5):
            answer+=sto[i]
        if(sto[i]>5):
            answer+=10-sto[i]
            sto[i+1]+=1
        if(sto[i]==5):
            answer+=sto[i]
            if(sto[i+1]>=5):
                sto[i+1]+=1
            
            
    

    
    return answer