#자연수 뒤집어 배열로 만들기
def solution(n):
    ans = [int(i) for i in str(n)]
    ans.reverse()
    return ans