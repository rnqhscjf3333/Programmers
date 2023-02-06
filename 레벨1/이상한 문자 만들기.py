#이상한 문자 만들기

def solution(s):
    answer = ""
    
    t=0
    for i in range(len(s)):
        if(t%2==0):
            answer+=s[i].upper()
        else:
            answer+=s[i].lower()
        t+=1
        if(s[i]==" "):
            t = 0
    
    return answer