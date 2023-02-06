#문자열 다루기 기본
def solution(s):
    
    if(len(s)==4 or len(s)==6):
        return s.isdigit()
    return False