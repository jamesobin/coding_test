def solution(n):
    num = []
    for i in range(1, 200):
        if i % 3 != 0 and i % 10 != 3 and i // 10 != 3 and i % 100 // 10 != 3:
            num.append(i)
    
    answer = num[n-1]

    return answer