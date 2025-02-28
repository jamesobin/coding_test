def solution(numbers):
    asc = sorted(numbers)
    
    if asc[-1] * asc[-2] >= asc[0] * asc[1]:
        answer = asc[-1] * asc[-2]
    elif asc[-1] * asc[-2] <= asc[0] * asc[1]:
        answer = asc[0] * asc[1]
        
    return answer