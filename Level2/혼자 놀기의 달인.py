#혼자 놀기의 달인
def solution(cards):
    answer = 0
    
    n = len(cards)
    
    openc = [0]*(n+1)
    
    i = 1
    itt = []

    while(i<=n):
        it = 0  
        
        while(True):
            if openc[i]==1:
                break
            openc[i]=1
            it+=1
            i = cards[i-1]
            
        if it>0:
            itt.append(it)
        i+=1
            
            
    print(itt)
    if len(itt)<2:
        return 0
    
    
    itt.sort(reverse = True)
    return itt[0]*itt[1]