#하샤드 수
def solution(x):
    answer = True
    
    ans = 0
    for i in str(x):
        ans+=int(i)
    if(x%ans==0):
        return True
    
    return False