lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
desired_servings = float(input("How many servings would you like to make?\n"))
multiplier = desired_servings / servings


print(f"Lemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{(multiplier*lemon_juice)/16:.2f} gallon(s) lemon juice")
print(f"{(multiplier*water)/16:.2f} gallon(s) water")
print(f"{(multiplier*agave_nectar)/16:.2f} gallon(s) agave nectar")