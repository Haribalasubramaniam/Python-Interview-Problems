def stocks(prices):
    left = 0
    right = 1
    max_profit = 0
    while right<len(prices):
        curr_profit = prices[right]-prices[left]
        if prices[left] < prices[right]:
            max_profit = max(max_profit,curr_profit)
        else:
            left = right
        right += 1
    return max_profit
        
        
        
    
    
prices1 = [7,1,5,3,6,4]
prices2 = [7,4,3,2]
print(stocks(prices1))
print(stocks(prices2))