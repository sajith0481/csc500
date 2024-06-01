food_item_name = input("Enter a food item name: ")
item_price = float(input("Enter item price: "))
item_quantity = int(input("Enter item quantity: "))

print(f"{item_quantity} {food_item_name} @ ${item_price:.2f} = ${item_price*item_quantity:.2f}")
print(f"Total cost: ${item_price*item_quantity:.2f}")

second_item_name = input("\nEnter second food item name: ")
second_item_price = float(input("Enter item price: "))
second_item_quantity = int(input("Enter item quantity: "))

print(f"{item_quantity} {food_item_name} @ ${item_price:.2f} = ${item_price*item_quantity:.2f}")
print(f"{second_item_quantity} {second_item_name} @ ${second_item_price:.2f} = ${second_item_price*second_item_quantity:.2f}")
print(f"Total cost: ${item_price*item_quantity + second_item_price*second_item_quantity:.2f}")

print("15% gratuity: ${:.2f}".format((item_price*item_quantity + second_item_price*second_item_quantity)*0.15))
print("Total with tip: ${:.2f}".format((item_price*item_quantity + second_item_price*second_item_quantity)*1.15))