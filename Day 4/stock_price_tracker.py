# Stock Price Tracker
# Given 30 days of stock prices:
# 1. Find the best day to buy and sell for maximum profit.
# 2. Calculate 7-day moving averages.
# 3. Find the most volatile week (highest price swing).


def find_max_profit(prices):
    min_price = prices[0]
    min_day = 1

    max_profit = 0
    buy_day = 1
    sell_day = 1

    for i in range(1, len(prices)):

        profit = prices[i] - min_price

        if profit > max_profit:
            max_profit = profit
            buy_day = min_day
            sell_day = i + 1

        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i + 1

    return buy_day, sell_day, max_profit


def moving_average(prices, window_size):
    averages = []

    for i in range(len(prices) - window_size + 1):
        window = prices[i:i + window_size]

        avg = round(sum(window) / window_size, 2)

        averages.append(avg)

    return averages


def most_volatile_week(prices):
    max_swing = 0
    start_day = 1
    high_price = 0
    low_price = 0

    for i in range(len(prices) - 6):
        window = prices[i:i + 7]

        high = max(window)
        low = min(window)

        swing = high - low

        if swing > max_swing:
            max_swing = swing
            start_day = i + 1
            high_price = high
            low_price = low

    return start_day, start_day + 6, high_price, low_price, max_swing


prices = [
    450, 455, 460, 448, 470, 475, 480,
    465, 458, 462, 470, 485, 490, 478,
    465, 455, 440, 430, 420, 410, 425,
    440, 460, 480, 377, 390, 410, 430,
    450, 470
]


buy_day, sell_day, profit = find_max_profit(prices)

print("\n----------MAXIMUM PROFIT----------")
print(f"Best Buy  : Day {buy_day} @ Rs.{prices[buy_day-1]}")
print(f"Best Sell : Day {sell_day} @ Rs.{prices[sell_day-1]}")
print(f"Max Profit: Rs.{profit}/share")


print("\n----------7-DAY MOVING AVERAGES----------")

averages = moving_average(prices, 7)

for i, avg in enumerate(averages, start=1):
    print(f"Window {i} (Day {i}-{i+6}): {avg}")


start, end, high, low, swing = most_volatile_week(prices)

print("\n----------MOST VOLATILE WEEK----------")
print(
    f"Week: Days {start}-{end} | "
    f"High: {high} | "
    f"Low: {low} | "
    f"Swing: {swing}"
)