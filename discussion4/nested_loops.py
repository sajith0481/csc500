# nested loop to print patterns
# row = 7
# # outer loop
# for i in range(1, row + 1):
#     # inner loop
#     for j in range(1, i + 1):
#         print("*", end=' ')
#     print("")

# list_fruits = ["apple", "banana", "cherry"]
# for fruit in list_fruits:
#     for letter in fruit:
#         print(letter, end='@')
#     print("")

# color = ["red", "green", "blue"]
# items = ["pen", "pencil", "eraser"]

# for c in color:
#     for i in items:
#         print(c, i)
#     print("")

#print right triangle
# for i in range(11):
#     for j in range(i):
#         print("*", end=' ')
#     print("")

# i = 11
# while i > 0:
#     j = 11
#     while j > i:
#         print("*", end=' ')
#         j -= 1
#     i -= 1
#     print("")

#Append 2 lists
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = []
# for i in list1:
#     for j in list2:
#         result.append(i+j)
# print(result)

#Multiplying 2 lists
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# for i in list1:
#     for j in list2:
#         if i == j:
#             continue
#         print(i, 'x', j, '= ', i*j)
#     print("")

# Perfect number
# a = 1
# while a <= 100:
#     sum = 0
#     for i in range(1, a):
#         if a % i == 0:
#             sum += i
#     if sum == a:
#         print('Perfect number:', a)
#     a += 1

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     count = 0
#     while count < 6:
#         print(fruit, end=' ')
#         count += 1
#     print()
