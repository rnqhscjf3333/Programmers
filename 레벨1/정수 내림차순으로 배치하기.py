#정수 내림차순으로 배치하기

def solution(n):
    answer = ""
    
    ans = [i for i in str(n)]
    ans.sort(reverse = True)
    
    for i in ans:
        answer+=i
    
    
    return int(answer)