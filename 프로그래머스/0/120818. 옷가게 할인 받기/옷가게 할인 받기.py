def solution(price):
    if price < 100000:
        answer = price
    elif 100000 <= price and price < 300000:
        answer = int(price * 0.95)
    elif 300000 <= price and price < 500000:
        answer = int(price * 0.9)
    else:
        answer = int(price * 0.8)
    
    return answer