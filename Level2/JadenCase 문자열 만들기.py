#JadenCase 문자열 만들기
def solution(s):
    
    isDown = True
    
    for i in range(len(s)):
        if(isDown):
            s = s[:i]+s[i].upper()+s[i+1:]
            isDown = False
        else:
            s = s[:i]+s[i].lower()+s[i+1:]
            
        if(s[i]==" "):
            isDown = True
    
    return s