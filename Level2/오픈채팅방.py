#오픈채팅방
def solution(record):
    answer = []
    
    dic = {}
    
    for i in range(len(record)-1,-1,-1):
        t = record[i].split()
        if(t[0]=="Change" or t[0]=="Enter"):
            if(t[1] not in dic):
                dic[t[1]] = t[2]
                
    for i in record:
        t = i.split()
        if(t[0]=="Enter"):
            answer.append(dic[t[1]]+"님이 들어왔습니다.")
        elif(t[0]=="Leave"):
            answer.append(dic[t[1]]+"님이 나갔습니다.")
    
    
    return answer