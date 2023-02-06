#신규 아이디 추천
def solution(new_id):
    answer = ''
    
    i = 0
    while(i<len(new_id)):
        if(new_id[i].isupper()):
            new_id=new_id.replace(new_id[i],new_id[i].lower())
        elif(not new_id[i].isalnum() and new_id[i] != "-" and new_id[i] != "_" and new_id[i] != "."):
             new_id=new_id.replace(new_id[i],"")
        elif(i>0 and new_id[i]=="." and new_id[i-1]=="."):
            new_id = new_id[:i]+new_id[(i+1):]
        else:
            i+=1
    if(len(new_id)>0 and new_id[0]=="."):
        new_id = new_id[1:]
    if(len(new_id)>0 and new_id[-1]=="."):
        new_id = new_id[:-1]
        
    if(len(new_id)==0):
        new_id="a"
        
    if(len(new_id)>15):
        new_id = new_id[:15]
        if(new_id[-1]=="."):
            new_id = new_id[:-1]
        
    while(len(new_id)<3):
        new_id+=new_id[-1]
            
    
    return new_id