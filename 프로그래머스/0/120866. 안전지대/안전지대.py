def solution(board):
    answer = 0
    
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 1:
                if j < (len(board) - 1):
                    if board[i][j+1] != 1:
                        board[i][j+1] = "x"
                if 1 <= j:
                    if board[i][j-1] != 1:
                        board[i][j-1] = "x"
                if i < (len(board[i]) - 1):
                    if board[i+1][j] != 1:
                        board[i+1][j] = "x"
                if i < (len(board[i]) - 1) and j < (len(board) - 1):
                    if board[i+1][j+1] != 1:
                        board[i+1][j+1] = "x"
                if i < (len(board[i]) - 1) and 1 <= j:
                    if board[i+1][j-1] != 1:
                        board[i+1][j-1] = "x"
                if 1 <= i:
                    if board[i-1][j] != 1:
                        board[i-1][j] = "x"
                if 1 <= i and j < (len(board) - 1):
                    if board[i-1][j+1] != 1:
                        board[i-1][j+1] = "x"
                if 1 <= i and 1 <= j:
                    if board[i-1][j-1] != 1:
                        board[i-1][j-1] = "x"
                    
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 0:
                answer += 1
            
    return answer