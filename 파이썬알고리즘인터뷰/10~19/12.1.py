# p12 : Best Time to Buy and Sell Stock

# brute-force solution

def max_profit(prices: list[int]) -> int:

    maximum = 0

    for i in range(0,len(prices)-1):
        for j in range(i+1,len(prices)):
            tmp = prices[j] - prices[i]
            if tmp > maximum:
                maximum = tmp

    return maximum

