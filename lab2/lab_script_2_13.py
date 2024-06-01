miles_per_gallon = float(input("Enter the miles per gallon of the car: "))
dollars_per_gallon = float(input("Enter the cost per gallon of gas in dollars: "))

print(f"The cost of driving 20 miles is ${(20/miles_per_gallon)*dollars_per_gallon:.2f}")
print(f"The cost of driving 75 miles is ${(75/miles_per_gallon)*dollars_per_gallon:.2f}")
print(f"The cost of driving 500 miles is ${(500/miles_per_gallon)*dollars_per_gallon:.2f}")