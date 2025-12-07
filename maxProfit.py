#leetcode - 121
def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        # elif price - min_price > max_profit:
        max_profit = max(price - min_price, max_profit)
    return max_profit
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    profit = maxProfit(prices)
    print("Maximum Profit:", profit)  # Output: 5