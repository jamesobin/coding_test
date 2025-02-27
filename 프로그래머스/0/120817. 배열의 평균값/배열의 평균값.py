def solution(numbers):
    size = len(numbers)
    sum = 0
    for i in range(0, size):
        sum += numbers[i]
        
    answer = sum / size
    
    return answer