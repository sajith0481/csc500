age = int(input("Enter your age: "))
weight = int(input("Enter your weight in pounds: "))
heart_rate = int(input("Enter your heart rate (in beats per minute): "))
time = int(input("Enter the number of minutes you exercised: "))

# Calculate the calories burned
calories_burned = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368
print(f"Calories burned: {calories_burned:.2f}")