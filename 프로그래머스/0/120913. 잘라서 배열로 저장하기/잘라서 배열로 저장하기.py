def solution(my_str, n):
    answer = []
    
    for i in range(0, len(my_str) // n):
        new_str = my_str[n*i:n*(i+1)]
        answer.append(new_str)
    
    if len(my_str) % n != 0:
        new_str = my_str[(len(my_str) // n) * n:]
        answer.append(new_str)
            
    return answer