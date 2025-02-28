def solution(numbers):
    desc = sorted(numbers, reverse=True)
    
    answer = desc[0] * desc[1]
    
    return answer