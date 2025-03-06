def solution(numlist, n):
    numlist.sort(reverse = True)
    answer = numlist
    sub = []
    
    for i in range(0, len(numlist)):
        sub.append(abs(numlist[i] - n))        
            
    for j in range(0, len(sub)):
        k = len(sub) - j
        for i in range(1, k):
            if sub[i-1] > sub[i]:
                temp = sub[i-1]
                sub[i-1] = sub[i]
                sub[i] = temp
                
                temp2 = answer[i-1]
                answer[i-1] = answer[i]
                answer[i] = temp2
        
    return answer