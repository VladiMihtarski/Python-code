from math import pi

r = float(input())
area = pi * r * r
perimeter = 2 * pi * r

print(f"{area:.2f} {perimeter:.2f}")


# from math import pi
#
# def calculate_circle(r):
#     area = pi * r * r
#     perimeter = 2 * pi * r
#     return area, perimeter
#
# def main():
#     r = float(input("Въведете радиус на кръга: "))
#     circle_area, circle_perimeter = calculate_circle(r)
#     print(f"{circle_area:.2f} {circle_perimeter:.2f}")
#
# if __name__ == "__main__":
#     main()
