# Array prices given. Where prices[i] is the price of a given stock on the "i"th day.
# You want to maximize your profit
# by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# return the maximum profit you can achieve from this transaction.
# if you cannot achieve any profit
# return 0.

# prices = [7, 1, 5, 3, 6, 4] Return 5.
# explanation: buy on day 2 (price = 1) and sell on day 5 [price = 6)
# profit = 6-1 = 5.

def buy_and_sell_stock(prices):
    max_sum = current_sum = 0
    for i in range(len(prices)-1):      # to check current ele and next ele, to not get out of price list boundaries, we use -1.
                                        # if we'll check the next ele of last ele, it wont exist in list and give error.
        current_sum = current_sum + prices[i + 1] - prices[i]   # Q:??? cur_sum = cur_sum + prices at index 1 + next element - previous element.
                                                                        # [7, 1, 5, 3, 6, 4] --> 1+5=6...6-1=5?
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum


test_list = [7, 1, 5, 3, 6, 4]
result = buy_and_sell_stock(test_list)
print(result)
