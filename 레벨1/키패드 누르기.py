#키패드 누르기
def solution(numbers, hand):
    answer = ''
    
    key = {}
    key[0] = [4,2]
    key[1] = [1,1]
    key[2] = [1,2]
    key[3] = [1,3]
    key[4] = [2,1]
    key[5] = [2,2]
    key[6] = [2,3]
    key[7] = [3,1]
    key[8] = [3,2]
    key[9] = [3,3]
    L=[4,1]
    R=[4,3]
    
    for i in numbers:
        if(i==1 or i==4 or i==7):
            answer += "L"
            L=key[i]
        elif(i==3 or i==6 or i==9):
            answer += "R"
            R=key[i]
        else:
            LM = abs(key[i][0]-L[0])+abs(key[i][1]-L[1])
            RM = abs(key[i][0]-R[0])+abs(key[i][1]-R[1])
            if(LM<RM):
                answer += "L"
                L=key[i]
            elif(LM>RM):
                answer += "R"
                R=key[i]
            else:
                if(hand == "right"):
                    answer += "R"
                    R=key[i]
                else:
                    answer += "L"
                    L=key[i]
    
    return answer