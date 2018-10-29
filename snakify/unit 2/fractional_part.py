# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
from decimal import *
x = Decimal(input())
y = int(x)

print(Decimal(x - y))