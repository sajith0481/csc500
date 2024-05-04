import array as arr

# List to store the closing prices of a stock over a period of time
prices = arr.array('d', [120.5, 122.75, 125.0, 123.5, 124.0, 125.5, 126.0])

# Define the number of shares owned
shares_owned = 50

# Calculate the total value of stocks for each day
total_values = arr.array('d', [price * shares_owned for price in prices])

# Print the total value of stocks for each day
for i in range(1, len(prices) + 1):
    print(f"The total value of stocks on day {i} is ${total_values[i - 1]}")
