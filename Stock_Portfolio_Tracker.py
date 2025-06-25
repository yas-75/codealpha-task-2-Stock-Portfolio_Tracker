# Simple Stock Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "INFY": 1600
}

total_investment = 0
investment_log = []

print("📈 Welcome to the Stock Tracker!\n")
print("Available Stocks:", ", ".join(stock_prices.keys()))

try:
    n = int(input("\nHow many different stocks do you want to track? "))

    for i in range(n):
        print(f"\nStock #{i+1}")
        stock_name = input("Enter stock symbol (e.g. AAPL, TSLA): ").strip().upper()

        if stock_name not in stock_prices:
            print("❌ Invalid stock name! Skipping this entry.")
            continue

        qty = int(input("Enter quantity: "))
        price = stock_prices[stock_name]
        value = qty * price
        total_investment += value

        investment_log.append(f"{stock_name} x {qty} @ ₹{price} = ₹{value}")

except ValueError:
    print("⚠️ Please enter valid numeric inputs only.")
    exit()

# Print Summary
print("\n🧾 Investment Summary:")
for line in investment_log:
    print(line)

print(f"\n💰 Total Investment Value: ₹{total_investment}")

# Save to file section with UTF-8 encoding
save = input("\nDo you want to save the summary in a file? (yes/no): ").strip().lower()
if save == "yes":
    try:
        with open("investment_summary.txt", "w", encoding="utf-8") as file:
            file.write("Stock Investment Summary\n")
            file.write("------------------------\n")
            for line in investment_log:
                file.write(line + "\n")
            file.write(f"\nTotal Investment Value: ₹{total_investment}")
        print("✅ Summary saved in 'investment_summary.txt'")
    except Exception as e:
        print("❗ Error saving file:", e)
else:
    print("📁 Summary not saved.")
