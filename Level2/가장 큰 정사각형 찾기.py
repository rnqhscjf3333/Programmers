#가장 큰 정사각형 찾기

def solution(board):

    answer = 0
    
    if(len(board)==1 or len(board[0])==1):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if(board[y][x]==1):
                    return 1

    for y in range(1,len(board)):
        for x in range(1, len(board[0])):
            if(board[y][x]==1):
                board[y][x] = min(board[y-1][x],board[y][x-1],board[y-1][x-1])+1
                answer = max(board[y][x],answer)
            

    return answer*answer