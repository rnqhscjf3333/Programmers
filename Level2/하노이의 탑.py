#하노이의 탑
def solution(n):
    answer = []
    hanoi(n,1,3,2, answer)
    
    
    return answer
def hanoi(n, from_nos, to_nos, aux_pos, answer):
        if n == 1:  # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
            answer.append([from_nos,to_nos])
            return answer
        hanoi(n-1, from_nos,aux_pos,to_nos,answer)
        answer.append([from_nos,to_nos])
        hanoi(n-1, aux_pos,to_nos,from_nos,answer)