def solution(n, numlist):
    size = len(numlist)
    
    answer = []
    
    for i in range(0, size):
        if numlist[i] % n == 0:
            answer.append(numlist[i])
    
    return answer