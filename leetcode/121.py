    

def maxProfit(prices):
    min_price=max(prices)
    answer=0
    
    for price in prices:
        min_price = min(min_price, price)
        answer = max(answer, price - min_price)

    return answer
    
print(maxProfit([7,1,5,3,6,4]))