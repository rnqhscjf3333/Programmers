#k진수에서 소수 개수 구하기
import string

def is_prime_number(x):#소수 함수
    i=2
    if x<=1:
        return False
    while(i*i<=x):
        if x % i == 0:
            return False
        i+=1
    return True 

#진법 변환
tmp = string.digits+string.ascii_uppercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, k):
    answer = 0
    
    t = convert(n,k)
    print(t)
    
    num = ""
    
    for i in t:
        if i != "0":
            num+=i
        elif num != "":
            if is_prime_number(int(num))== True:
                answer+=1
            num = ""
    if num != "" and is_prime_number(int(num))== True:
        answer+=1
            
    
    
    
    
    return answer