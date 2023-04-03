#다음 큰 숫자
def solution(n):
    answer = 0
    
    cnt = bin(n).count("1")
    
    while(True):
        n+=1
        if bin(n).count("1")==cnt:
            break
    
    return n