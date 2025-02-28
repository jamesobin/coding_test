def solution(strlist):
    size = len(strlist)
    
    answer = []
    
    for i in range(0, size):
        answer.append(len(strlist[i]))
    
    return answer