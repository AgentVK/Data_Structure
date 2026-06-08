prices = [7, 1, 5, 3, 6, 4]
min_price_so_far = prices[0]
max_profit = 0

buy_price = None
sell_price = None

for price in prices:
    if price < min_price_so_far:
        min_price_so_far = price
    
    current_profit = price - min_price_so_far

    if current_profit > max_profit:
        buy_price = min_price_so_far
        sell_price = price
        max_profit = current_profit
    
if max_profit == 0:
    print(f"No Profit {sell_price}:{buy_price}")
else:
    print("Buy Price :",buy_price)
    print("Sell Price :",sell_price)
    print("Max Profit :",max_profit)