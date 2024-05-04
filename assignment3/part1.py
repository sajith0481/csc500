# Get the charge for the food from the user
food_charge = float(input("Enter the charge for the food: "))

# Calculate the tip amount (18% of the food charge)
tip_amount = food_charge * 0.18

# Calculate the sales tax amount (7% of the food charge)
tax_amount = food_charge * 0.07

# Calculate the total price (food charge + tip amount + tax amount)
total_price = food_charge + tip_amount + tax_amount

# Display the amounts and total price
print('Tip amount: $', format(tip_amount, ".2f"))
print("Sales tax amount: $", format(tax_amount, ".2f"))
print("Total price: $", format(total_price, ".2f"))