def solution(survey, choices):
    RT=[0,0]
    CF=[0,0]
    JM=[0,0]
    AN=[0,0]
    
    sur = {}
    sur["R"] = 0
    sur["T"] = 0
    sur["C"] = 0
    sur["F"] = 0
    sur["J"] = 0
    sur["M"] = 0
    sur["A"] = 0
    sur["N"] = 0
    
    answer = ''
    
    for i in range(len(survey)):
        if(choices[i]==4):
            continue
        if(choices[i]<4):
            sur[survey[i][0]]+=4-choices[i]
        else:
             sur[survey[i][1]]+=choices[i]-4
    
    if(sur["R"]>=sur["T"]):
        answer+="R"
    else:
        answer+="T"
    if(sur["C"]>=sur["F"]):
        answer+="C"
    else:
        answer+="F"
    if(sur["J"]>=sur["M"]):
        answer+="J"
    else:
        answer+="M"
    if(sur["A"]>=sur["N"]):
        answer+="A"
    else:
        answer+="N"
        
    
    return answer