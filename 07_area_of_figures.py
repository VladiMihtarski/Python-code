from math import pi

figure = input("Enter figure type (square, rectangle, circle or triangle): ")

if figure == "square":
    side = float(input("Enter side length: "))
    area = side ** 2
elif figure == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
elif figure == "circle":
    radius = float(input("Enter radius: "))
    area = pi * radius ** 2
else: # assuming figure is triangle
    base = float(input("Enter base length: "))
    height = float(input("Enter height length: "))
    area = 0.5 * base * height

print(f"{area:.3f}")

# from math import pi
#
# figure = input("Enter figure type (square, rectangle, circle or triangle): ")
#
# if figure == "square":
#     area = float(input("Enter side length: ")) ** 2
# elif figure == "rectangle":
#     area = float(input("Enter length: ")) * float(input("Enter width: "))
# elif figure == "circle":
#     area = pi * float(input("Enter radius: ")) ** 2
# else:
#     area = 0.5 * float(input("Enter base length: ")) * float(input("Enter height length: "))
#
# print(f"{area:.3f}")
