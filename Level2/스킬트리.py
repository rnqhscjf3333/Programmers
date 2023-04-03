#스킬트리
def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        sk = skill
        for k in s:
            a = sk.find(k)
            if(a==0):
                sk = sk[1:]
            if(a>0):
                answer-=1
                break
        answer+=1
            
        
        
    return answer