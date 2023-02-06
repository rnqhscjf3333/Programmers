#소수 만들기
#소수는 함수 따로
def solution(nums):
    answer = 0
    
    nums.sort()
    for i in range(len(nums)-2):
        for t in range(i+1, len(nums)-1):
            for k in range(t+1, len(nums)):
                count = nums[i]+nums[t]+nums[k]
                print(count)
                if(is_prime_number(count)):
                    answer+=1
    return answer

def is_prime_number(x):#소수
    i=2
    while(i*i<=x):
        if x % i == 0:
            return False
        i+=1
    return True 