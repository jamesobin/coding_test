def solution(age):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    answer = ''
    
    sage = str(age)
    
    for i in range(0, len(sage)):
        answer += alphabet[int(sage[i])]
        
    return answer