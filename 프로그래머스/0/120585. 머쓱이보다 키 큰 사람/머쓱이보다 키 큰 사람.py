def solution(array, height):
    array.append(height)
    
    desc = sorted(array, reverse=True)
    
    answer = desc.index(height)
    
    return answer