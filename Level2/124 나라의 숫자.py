#124 나라의 숫자
#재귀
answer = ''
def solution(n):
    def sol(n):
        global answer
        if(n==1):
            answer+="1"
        elif(n==2):
            answer+="2"
        elif(n==3 or n==0):
            answer+="4"
        else:
            sol((n-1)//3)
            sol(n%3)
    
    
    sol(n)
    return answer