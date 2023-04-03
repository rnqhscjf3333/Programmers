#프린터
def solution(priorities, location):
    answer = 0
    ans = [i for i in range(len(priorities))]
    
    v=0
    while(True):
        if(priorities[0] != max(priorities)):
            priorities = priorities[1:]+[priorities[0]]
            ans = ans[1:]+[ans[0]]
        else:
            v+=1
            if(ans[0]==location):
                return v
            del priorities[0]
            del ans[0]