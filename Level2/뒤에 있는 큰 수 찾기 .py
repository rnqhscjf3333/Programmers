#뒤에 있는 큰 수 찾기
from collections import deque

def solution(numbers):
    answer = [-1]*len(numbers)
    ans = []
    
    
    dq = deque()
    dq2 = deque()
    
    for i in range(len(numbers)):
        if not dq or dq[-1]>=numbers[i]:
            dq.append(numbers[i])
            dq2.append(i)
        else:
            while dq and dq[-1]<numbers[i]:
                dq.pop()
                answer[dq2.pop()] = numbers[i]
            dq.append(numbers[i])
            dq2.append(i)

    
    
    return answer