def solution(array):
    size = len(array)
    half = len(array) // 2
    
    asc = sorted(array)
    answer = asc[half]
    
    return answer