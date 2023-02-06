#문자열 내림차순으로 배치하기
def solution(s):
    s = ''.join(sorted(s,reverse=True))
    return s