stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 400,
    "GOOGL": 150,
    "AMZN": 180
}

portfolio = []

while True:

    # ask stock
    stock = input("Enter stock name: ").upper()

    # Check if stock exists
    if stock not in stock_prices: 
        print("Stock not available. Please choose from:") 
        print(", ".join(stock_prices.keys())) 
        continue

    # ask quantity
    quantity = input("Enter quantity: ")

    # Check if quantity is valid 
    if not quantity.isdigit() or int(quantity) <= 0: 
        print("Please enter a valid positive quantity.")
        continue

    quantity = int(quantity)

    # Get stock price 
    price = stock_prices[stock]

    # calculate investment
    investment = stock_prices[stock] * quantity
    # add to portfolio
    portfolio.append([stock, quantity, price, investment])

    print(f"{stock} added successfully!") 
    print(f"Investment: ${investment}")

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice == "no":
        break

# Calculate total investment
total = 0
# Save portfolio to a file
with open("portfolio.txt", "w") as file:
    file.write("----- STOCK PORTFOLIO -----\n\n")

    for item in portfolio:
        stock = item[0]
        quantity = item[1]
        price = item[2]
        investment = item[3]

        file.write(f"Stock: {stock}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Price: ${price}\n")
        file.write(f"Investment: ${investment}\n")
        file.write("--------------------------\n")

    file.write(f"Total Investment: ${total}\n")

print("\nPortfolio saved to portfolio.txt")
