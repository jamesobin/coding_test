def solution(dots):
    answer = 0
    slope = []
    
    slope.append(((dots[0][0] - dots[1][0]) / (dots[0][1] - dots[1][1])) / ((dots[2][0] - dots[3][0]) / (dots[2][1] - dots[3][1])))
    slope.append(((dots[0][0] - dots[2][0]) / (dots[0][1] - dots[2][1])) / ((dots[1][0] - dots[3][0]) / (dots[1][1] - dots[3][1])))
    slope.append(((dots[0][0] - dots[3][0]) / (dots[0][1] - dots[3][1])) / ((dots[2][0] - dots[1][0]) / (dots[2][1] - dots[1][1])))
    
    if 1 in slope:
        answer = 1
    else:
        answer = 0
        
    return answer