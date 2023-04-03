#소수 찾기
def solution(numbers):
    ans = []
    
    def sol(st, num):
        global answer
        if(st != "" and int(st)>1 and int(st) not in ans and is_prime_number(int(st))==True):
            ans.append(int(st))
            
        if(num!=""):
            for i in range(len(num)):
                sol(st+num[i],num[:i]+num[i+1:])
    
    sol("", numbers)
    #print(ans)
    
    
    
    return len(ans)




def is_prime_number(x):#소수
    i=2
    while(i*i<=x):
        if x % i == 0:
            return False
        i+=1
    return True