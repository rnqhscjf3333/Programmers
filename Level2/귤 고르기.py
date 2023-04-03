#귤 고르기
def solution(k, tangerine):
    answer = 0
    
    n = len(tangerine)
    
    dic = {}
    
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
            
    ans = []
    for key, value in dic.items():
        ans.append(value)
    ans.sort()

    
    while(n>k):
        n-=ans[0]
        del ans[0]
    if n==k:
        return len(ans)
    else:
        return len(ans)+1