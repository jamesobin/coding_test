def solution(sides):
    asc = sorted(sides)
    
    if (asc[0] + asc[1]) > asc[2]:
        answer = 1
    else:
        answer = 2
    
    return answer