def solution(numbers, k):
    size = len(numbers)
    
    answer = numbers[(k - 1) * 2 % size]
    
    return answer