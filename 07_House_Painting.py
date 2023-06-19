x = float(input())
y = float(input())
h = float(input())

side_wall_area = 2 * x * y - 2 * (1.5 * 1.5)
front_back_wall_area = 2 * x * x - 1.2 * 2

total_wall_area = side_wall_area + front_back_wall_area

roof_rectangles_area = 2 * x * y
roof_triangles_area = 2 * (x * h / 2)

total_roof_area = roof_rectangles_area + roof_triangles_area

green_paint = total_wall_area / 3.4
red_paint = total_roof_area / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
