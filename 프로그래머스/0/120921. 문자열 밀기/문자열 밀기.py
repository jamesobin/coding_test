def solution(A, B):
    answer = 0
    count = 0
    
    for i in range(0, len(A)):
        if A == B:
            break
        else:
            A = A[-1] + A[:-1]
            count += 1
            continue
            
    if count == len(A):
        answer = -1
    else:
        answer = count
    
    return answer