name = input("What's your name:    ")
shape = int(input("What shape do you want? (1=square, 2=rectangular, or 3=cylindrical.)"))
h = float(input("What do you want the height of the pool to be? (float)"))

if shape == 1:
    b = int(input("Base edge length?"))
    print (b * b * h * 7.5)
    print(name)

elif shape == 2:
    rect_l = float(input("Rectangular length?"))
    rect_w = float(input("Rectangular width??"))
    print(rect_1 * rect_w * height * 7.5)
    print(name)

elif shape == 3:
    r = float(input("Cylinder radius?"))
    from math import pi
    print(r * r * pi * h * 7.5)
    print(name)

else:
    print("Choose valid shape")