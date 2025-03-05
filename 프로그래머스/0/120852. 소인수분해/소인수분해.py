def solution(n):
    tmp = n
    answer = []
    for i in range(2, n +1):
        while True:
            if tmp % i == 0:
                tmp = tmp // i
                if i not in answer:
                    answer.append(i)
                continue
                
            if tmp % i != 0:
                break
            
    return answer