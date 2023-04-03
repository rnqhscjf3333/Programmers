#주차 요금 계산
import datetime
import math

def solution(fees, records):
    answer = []
    
    dic1 = {}
    dic2 = {}
    
    i=0
    while i<len(records):
        rec = records[i].split()
        if rec[2]=="IN":
            dic1[rec[1]] = rec[0]
        else:
            dq1 = datetime.datetime.strptime(dic1[rec[1]], '%M:%S')
            dq2 = datetime.datetime.strptime(rec[0], '%M:%S')
            diff = dq2 - dq1
            if rec[1] not in dic2:
                dic2[rec[1]] = diff.seconds
            else:
                dic2[rec[1]] += diff.seconds
                
            del dic1[rec[1]]
        i+=1
        
    for i in dic1:
        dq1 = datetime.datetime.strptime(dic1[i], '%M:%S')
        dq2 = datetime.datetime.strptime("23:59", '%M:%S')
        diff = dq2 - dq1
        if i not in dic2:
            dic2[i] = diff.seconds
        else:
            dic2[i] += diff.seconds
        
    dic2 = sorted(dic2.items())
    print(dic2)
    
    for i in range(len(dic2)):
        if dic2[i][1]>fees[0]:
            answer.append(fees[1]+math.ceil((dic2[i][1]-fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])
    
    
    return answer