def solution(s):
    answer = [0 for i in range(len(s))]
    for i in range(len(s)):
        if(i==0):
            answer[i] = -1
        else:
            for t in range(i):
                print(s[i-t-1], end='')
                if(s[i-t-1]==s[i]):
                    answer[i] = t+1
                    break
                answer[i] = -1
    return answer