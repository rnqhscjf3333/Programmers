#두 개 뽑아서 더하기
def solution(numbers):
    answer = set()

    
    numbers.sort()
    
    for i in range(len(numbers)):
        for t in range(i+1, len(numbers)):
            answer.add(numbers[i]+numbers[t])

    answer = list(answer)
    answer.sort()
    
    return answer