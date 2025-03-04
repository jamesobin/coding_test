def solution(array):
    count = 0
    
    for i in range(0,len(array)):
        count += str(array[i]).count("7")
    return count