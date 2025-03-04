def solution(my_string):
    new_string = ""
    for i in range(0, len(my_string)):
        if my_string[i] not in new_string:
            new_string += my_string[i]
            
    return new_string