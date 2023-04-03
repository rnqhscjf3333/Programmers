#행렬의 곱셈
def solution(arr1, arr2):
    answer = []
    
    for a in range(len(arr1)):
        att = []
        for b in range(len(arr2[0])):
            
            at = 0
            for c in range(len(arr2)):
                at+=(arr1[a][c]*arr2[c][b])
            att.append(at)
        answer.append(att)
                
    
    
    
    return answer