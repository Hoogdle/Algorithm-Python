import sys

# solve with graph(visualization)
# O(n)
# max_profit could be find in situation that have 'local minimum(hopefully expect global minimum)'

def max_profit(prices: list[int]) -> int:
    profit = 0
    minimum = sys.maxsize # using sys library for using maximum number

    for price in prices:
        minimum = min(minimum, price)
        profit = max(profit, price - minimum)

    return profit

print(max_profit([7,1,5,3,6,4]))