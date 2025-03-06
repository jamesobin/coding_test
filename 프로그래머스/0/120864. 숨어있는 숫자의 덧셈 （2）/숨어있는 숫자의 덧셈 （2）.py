def solution(my_string):
    num = 0
    answer = 0

    for i in range(0, len(my_string)):
        if my_string[i].isnumeric():
            num = num * 10 + int(my_string[i])
        else:
            answer += num
            num = 0
    answer += num
    
    return answer