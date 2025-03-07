def solution(want, number, discount):
    product = []
    product_list = []
    
    for i in range(0, len(discount) - 9):
        product = discount[i:i+10]
        product_list.append(product)
        product_list[i].sort()
    
    new_want = []
    
    for i in range(0, len(want)):
        for j in range(0, number[i]):
            new_want.append(want[i])
            new_want.sort()
    
    count = 0
    
    for i in range(0, len(product_list)):        
        if product_list[i] == new_want:
            count += 1
                
    return count