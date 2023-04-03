#압축
dic = [""]
for i in range(65, 91):
    dic.append(chr(i))

def solution(msg):
    answer = []
    
    i=0
    while(i<len(msg)):
        mt = ""
        for t in range(i, len(msg)):
            mt+=msg[t]
            
            if(mt not in dic):
                dic.append(mt)
                
                answer.append(dic.index(mt[:-1]))
                i+=max(0,len(mt)-2)
                
                break
            if(t==len(msg)-1):
                answer.append(dic.index(mt))
                return answer
        i+=1
    
        
    #print(dic)
    return answer