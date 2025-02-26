def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        factorial = 1
        
        for j in range(2, i+1):
            factorial *= j
        
        if factorial <= n:
            answer = i
        else:
            break
    
    return answer