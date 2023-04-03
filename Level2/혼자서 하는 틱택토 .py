#혼자서 하는 틱택토
def solution(board):
    
    board2 = [[0,0,0],[0,0,0],[0,0,0]]
        
    Onum = 0
    Xnum = 0
    Owin = 0
    Xwin = 0
    
    for i in range(3):
        Onum+=board[i].count("O")
        Xnum+=board[i].count("X")
        
        if board[i] == "OOO":
            board2[i][0]+=1
            board2[i][1]+=1
            board2[i][2]+=1
            Owin+=1
        elif board[i] == "XXX":
            board2[i][0]-=1
            board2[i][1]-=1
            board2[i][2]-=1
            Xwin+=1
    
    if abs(Onum - Xnum)>=2 or Xnum>Onum:
        return 0
    
    for i in range(3):
        if board[0][i]=="O" and board[1][i]=="O" and board[2][i]=="O":
            board2[0][i]+=1
            board2[1][i]+=1
            board2[2][i]+=1
            Owin+=1
        elif board[0][i]=="X" and board[1][i]=="X" and board[2][i]=="X":
            board2[0][i]-=1
            board2[1][i]-=1
            board2[2][i]-=1
            Xwin+=1
    
    if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O": #대각선
        board2[0][0]+=1
        board2[1][1]+=1
        board2[2][2]+=1
        Owin+=1
    elif board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X": 
        board2[0][0]-=1
        board2[1][1]-=1
        board2[2][2]-=1
        Xwin+=1
    
    if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O": #대각선
        board2[0][0]+=1
        board2[1][1]+=1
        board2[2][2]+=1
        Owin+=1
    elif board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X": 
        board2[0][0]-=1
        board2[1][1]-=1
        board2[2][2]-=1
        Xwin+=1
        
    if Owin>0 and Xwin>0:
        return 0
    
    if Owin>0 and Onum<=Xnum:
        return 0
    if Xwin>0 and Onum!=Xnum:
        return 0
        
    numcount = 0
    for a in range(3):
        for b in range(3):
            if board2[a][b]>1 or board2[a][b]<-1:
                numcount+=1
                
                    
                
    if numcount>1:
        return 0
    
    
    return 1