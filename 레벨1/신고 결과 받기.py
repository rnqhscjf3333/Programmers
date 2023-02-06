def solution(id_list, report, k):
    ans1 = [[] for i in range(len(id_list))]
    ans2 = [0 for i in range(len(id_list))]

    
    i = 0
    
    reports = set(report)
    
    for i in reports:
        ans1[id_list.index(i.split()[1])].append(i.split()[0])
            
    for i in ans1:
        if(len(i)>=k):
            for t in i:
                ans2[id_list.index(t)]+=1
                

                                  
    return ans2