# Ask for the number of years
num_years = int(input("Enter the number of years: "))

# Initialize variables
total_rainfall = 0
num_months = num_years * 12

# Outer loop for each year
for year in range(1, num_years + 1):
    # Inner loop for each month
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for Year {year}, Month {month}: "))
        total_rainfall += rainfall

# Calculate average rainfall
average_rainfall = total_rainfall / num_months

# Display results
print(f"Number of months: {num_months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month in inches: {average_rainfall:.2f}")
