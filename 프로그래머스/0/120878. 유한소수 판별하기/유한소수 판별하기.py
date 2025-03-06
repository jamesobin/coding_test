def solution(a, b):
    while True:
        if b % 2 == 0:
            b = b // 2
            continue
        elif b % 5 == 0:
            b = b // 5
            continue
        else:
            break
    
    if b % a == 0 or a % b == 0:
        answer = 1
    else:
        answer = 2
        
    return answer