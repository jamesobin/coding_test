def solution(arr, query):
    answer = []
    
    for i in range(0, len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    
    answer = arr
    
    return answer