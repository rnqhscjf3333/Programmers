def solution(s):
    answer = 0
    x=s[0]
    
    count1=0
    count2=0
    
    for i in range(len(s)):
        if(count1>0 and count1 == count2):
            x=s[i]
            answer+=1
            count1=0
            count2=0
            
            print(s[i])
        
        if(s[i]==x):
            count1+=1
        else:
            count2+=1
        if(i==len(s)-1):
            answer+=1

    return answer