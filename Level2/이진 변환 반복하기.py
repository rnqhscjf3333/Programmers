#이진 변환 반복하기
def solution(s):
    a=0
    b=0
    return sol(s,a,b)


def sol(s,a,b):
    a+=1
    b+=s.count("0")
    
    s=bin(s.count("1"))[2:]
    
    if(s=="1"):
        return [a,b]
    
    return sol(s,a,b)
        