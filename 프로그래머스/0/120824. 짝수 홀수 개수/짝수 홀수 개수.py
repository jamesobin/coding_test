def solution(num_list):
    evenCount = 0
    oddCount = 0
    
    for i in range(0, len(num_list)):
        if num_list[i] % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    
    answer = [evenCount, oddCount]
    
    return answer