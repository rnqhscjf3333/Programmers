#가장 큰 수
#거수정렬
#자리수 같게 바꾸고 비교
#숫자 앞자리 0이면 지우기


def solution(numbers):
    answer = ""
    
    num = []
    
    t=0
    for i in numbers:
        num.append([(str(i)*5)[:5],t])
        t+=1
    
    
    num.sort(reverse = True, key=lambda x: (int(x[0])))
    
    for i in num:
        answer+=str(numbers[i[1]])
        
    
    return str(int(answer))