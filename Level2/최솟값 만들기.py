#최솟값 만들기
def solution(A,B):
    answer = 0
    A.sort()
    B.sort()

    for i in range(len(A)):
        if(A[0]*B[-1]<=A[-1]*B[0]):
            answer+=A[0]*B[-1]
            del A[0]
            del B[-1]
        else:
            answer+=A[-1]*B[0]
            del A[-1]
            del B[0]

    return answer