def solution(keyinput, board):
    answer = [0, 0]
    
    for i in range(0, len(keyinput)):
        if keyinput[i] == "right":
            if answer[0] < board[0] // 2:
                answer[0] += 1
        elif keyinput[i] == "left":
            if -(board[0] // 2) < answer[0]:
                answer[0] -= 1 
        elif keyinput[i] == "up":
            if answer[1] < board[1] // 2:
                answer[1] += 1
        elif keyinput[i] == "down":
            if -(board[1] // 2) < answer[1]:
                answer[1] -= 1
            
    return answer