#연속 부분 수열 합의 개수
#중복 체크하는거보다 set쓰면 훨씬 빨라짐
def solution(elements):
    answer = 0
    sums = elements
    
    
    n = len(elements)
    elements += elements
    
    for a in range(n):
        for b in range(a+2,a+n+1):
            sums.append(sum(elements[a:b]))
    
    return len(set(sums))