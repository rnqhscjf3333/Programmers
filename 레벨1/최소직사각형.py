#최소직사각형
def solution(sizes):
    answer = 0
    
    x=0
    y=0
    for i in sizes:
        if(i[0]<i[1]):
            x = max(i[0],x)
            y = max(i[1],y)
        else:
            y = max(i[0],y)
            x = max(i[1],x)
    answer = x*y
    
    return answer