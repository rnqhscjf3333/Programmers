#최댓값과 최솟값
def solution(s):
    answer = ''
    
    maxi=-10000
    mini = 10000
    
    for i in s.split():
        if(int(i)>int(maxi)):
            maxi=i
        if(int(i)<int(mini)):
            mini = i
    
    
    return mini+" "+maxi