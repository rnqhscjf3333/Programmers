#파일명 정렬
def solution(files):
    answer = []
    
    ans = []
    for i in files:
        ans2 = ["","",""]
        t=0
        for t in range(len(i)):
            if(not i[t].isdigit()):
                ans2[0]+=i[t]
            else:
                break
        while(t<len(i)):
            if(i[t].isdigit()):
                ans2[1]+=i[t]
            else:
                break
            t+=1
        while(t<len(i)):
            ans2[2]+=i[t]
            t+=1
        #print(ans2)
        ans.append(ans2)
        
    ans.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    for i in ans:
        answer.append(i[0]+i[1]+i[2])
    
    return answer