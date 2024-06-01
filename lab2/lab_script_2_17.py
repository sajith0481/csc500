num = int(input("Enter a number between 32 and 126: "))
float_num = float(input("Enter a floating point number: "))
char_num = input("Enter a character: ")[0]
string_num = str(input("Enter a string: "))
num_char = chr(num)

print(f"{num} {float_num} {char_num} {string_num}")
print(f"{string_num} {char_num} {float_num} {num}")
print(f"{num} converted to a character is {num_char}")