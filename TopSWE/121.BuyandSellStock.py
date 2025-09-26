# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Brute Force Approach {SHit coz not applicable for large arrays}
def maxProfit(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n):  # Buy day
        for j in range(i + 1, n):  # Sell day
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit

# Optimal {SLIDING WINDOW}
def maxProfit(prices):
    l,r=0,1
    maxP=0
    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            maxP=max(profit,maxP)
        else:
            l=r
        r+=1
    return maxP
        

# Optimal {SINGLE PASS APPROACH}
def maxProfit(prices):
    minP=float(inf)
    maxP=0
    for i in prices:
        if i < minP:
            minP=i
        else:
            maxP=max(maxP,i-minP)
    return maxP
