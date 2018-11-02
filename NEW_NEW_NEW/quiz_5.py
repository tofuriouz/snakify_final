print("Give integer values for A (feet climbed during the day), B (feet fell at night) and H (distnace climbed up)")
print("A must be greater than B")
a = int(input("A:__"))
b = int(input("B:__"))
h = int(input("H:__"))
if a < b:
    print("A needs to be greater than B")
    exit()
delta = a - b
days =  h / delta
print(days)