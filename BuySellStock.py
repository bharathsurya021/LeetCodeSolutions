def maxProfit(prices):
    minPrice = prices[0]
    maxDiff = -10e8
    if len(prices) < 2:
        return 0
    for price in prices:
        maxDiff = max(maxDiff, price - minPrice)
        minPrice = min(minPrice, price)
    return maxDiff


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
