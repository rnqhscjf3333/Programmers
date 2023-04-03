#프렌즈4블록
def solution(m, n, board):
    answer = 0
    
    while(True):
        ans = []
        for a in range(m-1):
            for b in range(n-1):
                if(board[a][b] != "0" and board[a][b]==board[a][b+1] and board[a][b]==board[a+1][b] and board[a][b]==board[a+1][b+1]):
                    for a1 in range(a,a+2):
                        for b1 in range(b,b+2):
                            if([a1,b1] not in ans):
                                ans.append([a1,b1])
        for a, b in ans:
            while(a>0):
                board[a] = board[a][:b] + board[a-1][b] +board[a][b+1:]
                a-=1
            board[a] = board[a][:b] + "0" +board[a][b+1:]
            answer+=1
            
        
                
        if(len(ans)==0):
            break
    
    #print(board)
    return answer