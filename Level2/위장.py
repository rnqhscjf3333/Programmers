#위장
#(x+a)(x+b)(x+c) = x3 + (a+b+c)x2 + (ab+bc+ca)x + (abc)
def solution(clothes):
    answer = 0
    
    ans = {}
    for i in clothes:
        if(i[1] not in ans):
            ans[i[1]] =1
        else:
            ans[i[1]] +=1
    print(ans)
            
    for key, value in ans.items():
        if(answer==0):
            answer=value+1
        else:
            answer*=(value+1)
    
    return answer-1