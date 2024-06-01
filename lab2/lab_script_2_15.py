import math
from math import pow, sqrt

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
z = float(input("Enter another number: "))

value_1 = pow(x, z)
value_2 = pow(x,pow(y, z))
value_3 = abs(x-y)
value_4 = math.sqrt(pow(x, z))

print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(value_1, value_2, value_3, value_4))