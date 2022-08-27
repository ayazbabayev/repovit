# Array prices given. Where prices[i] is the price of a given stock on the "i"th day.
# Find maximum profit you can achieve.

# You may complete as many transactions as you like:
# (buy one and sell one share of the stock multiple times).

# ex. prices = [7, 1, 5, 3, 6, 4] Return 7.
# explanation: buy on day 2 (price = 1) and sell on day 3 [price = 5)
# profit = 5-1 = 4.

# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

def buy_and_sell_stock2(prices):
    maximum = 0
    for i in range(0, len(prices)-1):                           #
        if prices[i+1] > prices[i]:                             #
            maximum = maximum + prices[i + 1] - prices [i]      #

    return maximum

test_result = [7, 1, 5, 3, 6, 4]
result = buy_and_sell_stock2(test_result)
print(result)