def solution(number, limit, power):
    answer = []
    for i in range(number):
        if(getMyDivisor(i+1)>limit):
            answer.append(power)
        else:
            answer.append(getMyDivisor(i+1))
    
    return sum(answer)

def getMyDivisor(n):

    divisorsList = 0

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList+=1
            if ( (i**2) != n) : 
                divisorsList+=1

    return divisorsList