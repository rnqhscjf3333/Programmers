#방금그곡
def solution(m, musicinfos):
    answer = ''
    answ = []
    
    i=1
    while(i<len(m)):
        if(m[i]=='#'):
            if(m[i-1]=='A'):
                m = m[:i-1]+'1'+m[i+1:]
            elif(m[i-1]=='C'):
                m = m[:i-1]+'2'+m[i+1:]
            elif(m[i-1]=='D'):
                m = m[:i-1]+'3'+m[i+1:]
            elif(m[i-1]=='E'):
                m = m[:i-1]+'4'+m[i+1:]
            elif(m[i-1]=='F'):
                m = m[:i-1]+'5'+m[i+1:]
            elif(m[i-1]=='G'):
                m = m[:i-1]+'6'+m[i+1:]
            
        i+=1
    #print(m)
                
    
    for mu in musicinfos:
        mus = mu.split(",")
        
        i=1
        while(i<len(mus[3])):
            if(mus[3][i]=='#'):
                if(mus[3][i-1]=='A'):
                    mus[3] = mus[3][:i-1]+'1'+mus[3][i+1:]
                elif(mus[3][i-1]=='C'):
                    mus[3] = mus[3][:i-1]+'2'+mus[3][i+1:]
                elif(mus[3][i-1]=='D'):
                    mus[3] = mus[3][:i-1]+'3'+mus[3][i+1:]
                elif(mus[3][i-1]=='E'):
                    mus[3] = mus[3][:i-1]+'4'+mus[3][i+1:]
                elif(mus[3][i-1]=='F'):
                    mus[3] = mus[3][:i-1]+'5'+mus[3][i+1:]
                elif(mus[3][i-1]=='G'):
                    mus[3] = mus[3][:i-1]+'6'+mus[3][i+1:]
            i+=1
       # print(mus[3])
        
        
        a = [int (i) for i in mus[0].split(':')] 
        b = [int (i) for i in mus[1].split(':')] 
        ti = 0
        
        ti+=(b[0]-a[0])*60
        
        ti+=(b[1]-a[1])
        
        ans = ''
        for i in range(ti//len(mus[3])):
            ans+=mus[3]
        for i in range(ti%len(mus[3])):
            ans+=mus[3][i]
            
        if(m in ans):
            answ.append(mus[2]+','+str(ti))
            

            
    
    if(len(answ)==0):
        return "(None)"
    maxlen = 0
    maxt = ''
    
    for i in answ:
        t = i.split(',')
        if(maxlen<int(t[1])):
            maxt = t[0]
            maxlen = int(t[1])
    return maxt