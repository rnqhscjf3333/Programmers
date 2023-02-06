#로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = []
    
    maxi = 0
    mini = 0
    
    for i in lottos:
        if(i==0):
            maxi+=1
        else:
            if(win_nums.count(i)>0):
                maxi+=1
                mini+=1


    maxi=7-maxi
    mini=7-mini
    if(maxi>6):
        maxi=6
    if(mini>6):
        mini=6
    return [maxi, mini]