def max_profit(max_trades, daily_prices):
    if not daily_prices:
        return 0

    buy = [-float('inf')] * (max_trades + 1)
    sell = [0] * (max_trades + 1)

    for price in daily_prices:
        for t in range(1, max_trades + 1):
            buy[t] = max(buy[t], sell[t-1] - price)
            sell[t] = max(sell[t], buy[t] + price)

    return sell[max_trades]


# Example usage
max_trades = 2
daily_prices = [2000, 4000, 1000]
print(max_profit(max_trades, daily_prices))  

daily_prices = [1000, 2000, 3000, 4000]
print(max_profit(max_trades, daily_prices)) 
