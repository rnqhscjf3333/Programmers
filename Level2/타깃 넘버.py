#타깃 넘버
def solution(numbers, target):
    answer = 0
    
    return sol(numbers, target)
    
    
    return answer

def sol(numbers, target):
    #print(numbers, target)
    if(len(numbers)>1):
        return sol(numbers[1:], target-numbers[0])+sol(numbers[1:], target+numbers[0])
    
    if(target+numbers[0] ==0 or target-numbers[0]==0):
        return 1
    else:
        return 0