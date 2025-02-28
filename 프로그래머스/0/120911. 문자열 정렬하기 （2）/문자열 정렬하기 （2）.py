def solution(my_string):
    my_string = my_string.lower()
    answer = ""
    
    answer = answer.join(sorted(my_string))
    
    return answer