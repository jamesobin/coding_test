def solution(dots):
    x_list = []
    y_list = []
    for i in range(0, 4):
        if dots[i][0] not in x_list:
            x_list.append(dots[i][0])
        if dots[i][1] not in y_list:
            y_list.append(dots[i][1])
            
    for i in range(0, 2):
        width = abs(x_list[0] - x_list[1])
        height = abs(y_list[0] - y_list[1])
        
    answer = width * height
    
    return answer