num = int(input())
a = num % 10
b = ((num % 100 - a) / 10)

x = a * 10
print(x + b)
