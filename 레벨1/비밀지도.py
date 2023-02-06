#비밀지도
def solution(n, arr1, arr2):
    answer = ["" for i in range(n)]
    
    for i in range(n):
        for t in range(2, len(bin((arr1[i] | arr2[i])))):
            if(bin((arr1[i] | arr2[i]))[t]=="1"):
                answer[i]+="#"
            else:
                answer[i]+=" "
        while(len(answer[i])<n):
              answer[i] = " "+answer[i]
    
    
    return answer