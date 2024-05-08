# i = 0
# while i < 10:
#     i += 1
#     print(i, end='# ')
#     print()

# count = 0
# while count < 5:
#     print("The condition is true")
#     count = count + 1
# print("End of Loop")

# while True:
#     print("Please type your name.")
#     name = input()
#     if name == 'Joe':
#         break
# print("Thank you! You typed the correct name.")

# LCM of 4 and 7
# x = 0
# while True:
#     x += 1
#     if not(x % 4 or x % 7):
#         break
# print("The LCM of 4 and 7 is", x)

# i = 0
# while i < 10:
#     i += 1
#     if i == 6:
#         continue
#     print(i)

# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("i is not less than 5")

# a = [1,2,3,4,5]
# while a:
#     print(a.pop())
# else:
#     print("There are no elements in the list.")

# Avg of positive numbers
# num = 0
# count = 0
# sum = 0
# while num >= 0:
#     num = int(input("Enter a positive number: "))
#     if num >= 0:
#         sum += num
#         count += 1
# avg = sum / count
# print("The average of the positive numbers is:", avg)

# Guess the number
# import random
# n = random.randint(1, 100)
# print("The random number is:", n)
# guess = int(input("Enter your guess (1-100): "))
# while n != guess:
#     if guess < n:
#         print("Your guess is too low.")
#         guess = int(input("Enter your guess (1-100): "))
#     elif guess > n:
#         print("Your guess is too high.")
#         guess = int(input("Enter your guess (1-100): "))
#     else:
#         print("Congratulations! You guessed the correct number.")
#         break
#     print()

# nested loop to print patterns
# row = 7
# # outer loop
# for i in range(1, row + 1):
#     # inner loop
#     for j in range(1, i + 1):
#         print("*", end=' ')
#     print("")

