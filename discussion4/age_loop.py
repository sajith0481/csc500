# age =-1
# while age < 0 or age > 120:
#     age =int(input("Enter age: "))
#     #age = convert_to_integer(age)

#     if age < 0 or age > 120:

#         print("Error: Age must be between 0 and 120")

#     else:

#         print("Thank you.")

# print("Valid age entered:", age)

# age = -1
# while age < 0 or age > 120:
#     age = input("Enter a valid age between 0 and 120: ")
#     age = int(age)

# print("Valid age entered:", age)

# num = 15

# while num > 1:
#     num = num/2
#     print(num)

Grades = [80, 76, 100, 54, 85, 36, 97, 58, 69]
Grades.sort(reverse=True)  # Sort grades in descending order

n = 4
print("Highest Grades:")
for i in range(n):
    print(f"{i+1}. {Grades[i]}")