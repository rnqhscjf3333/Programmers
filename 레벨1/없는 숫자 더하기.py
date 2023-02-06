#없는 숫자 더하기
def solution(numbers):
    answer = 0
    
    ans = [i for i in range(10)]
    
    for i in numbers:
        ans.remove(i)
        
    
    return sum(ans)