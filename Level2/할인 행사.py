#할인 행사

def solution(want, number, discount):
    answer = 0
    
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    print(dic)
    
    for i in range(len(discount)-9):
        if discount[i] in dic:
            dic2 = dic.copy()
            ist = True
            for t in discount[i:i+10]:
                if t not in dic2 or dic2[t]==0:
                    ist = False
                    break
                else:
                    dic2[t]-=1
            if ist == True:
                answer+=1
    
    
    
    
    return answer