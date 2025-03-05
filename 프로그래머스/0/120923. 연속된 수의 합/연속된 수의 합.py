def solution(num, total):
    answer = []
    sum = 0
    
    for i in range(0, num):
        sum += i
        
    sub = (total - sum) / num
    
    for j in range(0, num):
        answer.append(j + sub)
        
    return answer