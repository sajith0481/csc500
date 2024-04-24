def check_positive(number):
    print(f"Checking if {number} is positive...")
    return number > 0


def check_negative(number):
    print(f"Checking if {number} is negative...")
    return number < 0


# Example using the 'and' operator
print("Testing 'and' short-circuiting:")
number = 0
if check_positive(number) and check_negative(number):
    print(f"{number} is both positive and negative (impossible!)")
else:
    print(f"{number} is not both positive and negative.")

print("\n")  # Adding a newline for clearer separation in output

# Example using the 'or' operator
print("Testing 'or' short-circuiting:")
number = 10
if check_positive(number) or check_negative(number):
    print(f"{number} is either positive or negative.")
else:
    print(f"{number} is neither positive nor negative.")
