def solution(sides):
    count = 0
    
    for i in range(1, sides[0] + sides[1]):
        sides.append(i)
        sides.sort()
        
        if (sides[0] + sides[1]) > sides[2]:
            count += 1
            
        sides.remove(i)
    
    return count