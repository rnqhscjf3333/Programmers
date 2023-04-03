#멀쩡한 사각형
#곱하기를 먼저하고 나누기
#힌트봄
def solution(w,h):
    answer = 0
    
    if(w==h):
        return w*h-w
    
    for i in range(1,w):
        answer+=(h * i)//w
    
    return answer*2