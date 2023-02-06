#크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    
    doll = []
    
    for i in moves:
        for t in range(len(board)):
            if(board[t][i-1]==0):
                continue
            else:
                if(len(doll)==0):
                    doll.append(board[t][i-1])
                else:
                    if(doll[-1]==board[t][i-1]):
                        del doll[-1]
                        answer+=2
                    else:
                        doll.append(board[t][i-1])
                board[t][i-1]=0
                break
        
    
    
    
    return answer