def solution(i, j, k):
    answer = 0
    
    for num in range(i, j+1):
        snum = str(num)
        answer += snum.count(str(k))
        
    return answer