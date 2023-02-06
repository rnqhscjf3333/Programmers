#모의고사
def solution(answers):
    answer = []
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1 = 0
    count2 = 0
    count3 = 0
    
    for i in range(len(answers)):
        if(answers[i] == ans1[i%5]):
            count1+=1
        if(answers[i] == ans2[i%8]):
            count2+=1
        if(answers[i] == ans3[i%10]):
            count3+=1
    if(count1 == max(count1, count2,count3)):
        answer.append(1)
        
    if(count2 == max(count1, count2,count3)):
        answer.append(2)
        
    if(count3 == max(count1, count2,count3)):
        answer.append(3)
        
    return answer