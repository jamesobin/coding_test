def solution(numbers):
    size = len(numbers)
    
    for i in range(0, size):
        numbers[i] = numbers[i] * 2
    answer = numbers
    return answer