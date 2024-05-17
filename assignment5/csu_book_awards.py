# Ask the user to enter the number of books purchased
num_books = int(input("Enter the number of books purchased this month: "))

# Calculate the points based on the number of books purchased
if 0 <= num_books <= 1:
    points = 0
elif 2 <= num_books <= 3:
    points = 5
elif 4 <= num_books <= 5:
    points = 15
elif 6 <= num_books <= 7:
    points = 30
elif num_books >= 8:
    points = 60
else:
    points = "Invalid input"

# Display the number of points awarded
print("Points awarded:", points)
