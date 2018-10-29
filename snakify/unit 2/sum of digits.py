# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
x = int(input())
a = x % 10
f = (((x % 100) - a) / 10)
c = ((x - x % 100) / 100)
print(a + f + c)
