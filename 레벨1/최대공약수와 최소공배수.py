#최대공약수와 최소공배수
import math
def solution(n, m):

    #return [math.gcd(n,m), math.lcm(n,m)] #lcm은 3.9 이상에서만됨
    
    return [gcd(n,m), lcm(n,m)]
    
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)