def solution(X, Y):
    answer = ''
    
    ast = False
    
    for i in ['9','8','7','6','5','4','3','2','1','0']:
        a=X.count(i)
        b=Y.count(i)
        if(min(a,b)>0):
            for t in range(min(a,b)):
                answer+=i
                if(i!='0'):
                    ast = True
                    
                    
    if(len(answer)==0):
        return '-1'
    
    if(ast == False):
        return '0'

    

    return answer