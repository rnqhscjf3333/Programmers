#서울에서 김서방 찾기
def solution(seoul):
    answer = ''
    
    for i in range(len(seoul)):
        if(seoul[i]=="Kim"):
            return "김서방은 "+str(i)+"에 있다"
    
    return answer