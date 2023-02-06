#행렬의 덧셈
def solution(arr1, arr2):
    answer = [[] for i in range(len(arr1))]
    
    for i in range(len(arr1)):
        for t in range(len(arr1[i])):
            answer[i].append(arr1[i][t]+arr2[i][t])
    
    
    return answer