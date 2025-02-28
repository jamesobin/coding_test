def solution(num, k):
    num = str(num)
    k = str(k)
    if k in num:
        for i in range(0, len(num)):
            if num[i] == k:
                answer = i + 1
                break
    else:
        answer = -1                
    
    return answer