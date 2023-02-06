#문자열 내 마음대로 정렬하기
def solution(strings, n):
    for a in range(len(strings)-1):
        for b in range(a, len(strings)):
            if(strings[a][n]>strings[b][n]):
                t = strings[a]
                strings[a] = strings[b]
                strings[b] = t
            if(strings[a][n]==strings[b][n]):
                t = [strings[a], strings[b]]
                t.sort()
                strings[a] = t[0]
                strings[b] = t[1]
                
    return strings