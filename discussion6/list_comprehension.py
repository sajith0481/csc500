# names = ["mariya", "joe", "jane", "jim", "jessica"]
# new_names = []

# for n in names:
#     if n.islower():
#         n = n.capitalize()
#     else:
#         n = "Relax " + n.capitalize()
#     new_names.append(n)

# names = new_names
# print(names)


# names = ["mariya", "joe", "jane", "jim", "jessica"]
# names = [
#     n.capitalize() if n.islower() 
#     else "Relax " + n.capitalize() 
#     for n in names
# ]
# print(names)

# my_string = "hi442nm233ag2"
# new_string = "".join(
#     ["d" if i=="4"
#      else "e" if i=="2"
#      else "s" if i=="3"
#      else i
#      for i in my_string ]
# )

# print(new_string)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # for fruit in fruits:
# #     print(fruit)
# [print(fruit) for fruit in fruits]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# new_fruits = []

# for fruit in fruits:
#     fruit = fruit.upper()
#     new_fruits.append(fruit)

# fruits = new_fruits
# print(fruits)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# bits = [False, True, False, True, True, True, False, False, True, False]
# new_bits = []

# for bit in bits:
#     if bit == True:
#         new_bits.append(1)
#     else:
#         new_bits.append(0)

# print(bits)
# print(new_bits)

# bits = [1 if bit == True else 0 for bit in bits]
# print(bits)

my_string = "HelloMyNameIsMariya"
my_string = "".join(
    [i if i.islower() else " " + i.lower() if i in ["N","I"] else " " + i for i in my_string])[1:]
print(my_string)