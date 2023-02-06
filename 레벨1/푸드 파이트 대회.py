def solution(food):
    answer = ''
    answer1 = ''
    for i in range(len(food)):
        if(i==0):
            continue
        for t in range(food[i]//2):
            answer+=str(i)
            answer1 = str(i)+answer1
        
    return answer + '0' + answer1