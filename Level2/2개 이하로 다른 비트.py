#2개 이하로 다른 비트
#시간 초과
def solution(numbers):
    answer = []
    
    for i in numbers:
        if(i%2==0):
            answer.append(i+1)
        else:
            it = bin(i)[2:]
            if(it.count("1") == len(it)):
                answer.append(int("0b"+"10"+it[1:],2))
            else:
                for i in range(len(it)-1, -1,-1):
                    if it[i]=="0":
                        it = it[:i]+"10"+it[i+2:]
                        answer.append(int(it,2))
                        break
        
    return answer