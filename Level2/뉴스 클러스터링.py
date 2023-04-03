#뉴스 클러스터링
def solution(str1, str2):
    answer = 0
    
    ans = {}
    
    str1=str1.upper()
    str2=str2.upper()
    
    for i in range(len(str1)-1):
        st = str1[i:i+2]
        if(st.isalpha() == False):
            continue
        if(st in ans):
            ans[st] = [ans[st][0]+1,ans[st][1]]
        else:
            ans[st] = [1,0]

        
    for i in range(len(str2)-1):
        st = str2[i:i+2]
        if(st.isalpha() == False):
            continue
        if(st in ans):
            ans[st] = [ans[st][0],ans[st][1]+1]
        else:
            ans[st] = [0,1]
            
    #print(ans)
            
    ry = 0
    gk = 0
    for key, value in ans.items():
        ry+=min(value)
        gk+=max(value)
    if(gk==0):
        return 65536
    return int((ry/gk)*65536)