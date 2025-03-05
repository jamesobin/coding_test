def solution(array, n):
    array.sort(reverse=True)
    
    min_sub = abs(array[0] - n) 
    
    for i in range(0, len(array)):
        sub = abs(array[i] - n)
        
        if sub <= min_sub:
            min_sub = sub
            answer = array[i]

    return answer