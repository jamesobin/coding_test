def solution(s1, s2):
    size1 = len(s1)
    
    count = 0
    for i in range(0, size1):
        if s1[i] in s2:
            count += 1
        
    answer = count
    
    return answer