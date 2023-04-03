#n진수 게임
import string

def solution(n, t, m, p):
    answer = ''
    
    ans = ""
    ans2 = 0
    
    while(len(ans)<t*m+p-1):
        ans+=convert(ans2,n)
        ans2+=1
    #print(ans)
    
    for i in range(t):
        print(i*m+p-1)
        answer+=ans[i*m+p-1]
    
    return answer

#진법 변환
tmp = string.digits+string.ascii_uppercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

solution(16,16,2,2)