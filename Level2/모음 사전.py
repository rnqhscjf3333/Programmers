#모음사전
import sys
sys.setrecursionlimit(10**5)
answer = 0
def solution(word):
    dic = ["A","E","I","O","U"]
    
    
    def sol1(wo, num):
        if(wo[num] != "U"):
            return wo[:num]+dic[dic.index(wo[num])+1]+wo[num+1:]
        else:
            return sol1(wo[:num],num-1)
    
    
    def sol(wo):
        global answer
        answer+=1
        if(len(wo)<5):
            wo+="A"
        else:
            wo = sol1(wo,4)
            
        if(wo == word):
            return 0
        else:
            sol(wo)
    

    
    sol("")
    
    return answer