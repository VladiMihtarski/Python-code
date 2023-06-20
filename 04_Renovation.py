from math import ceil

wall_height = int(input())
wall_width = int(input())
percent_not_painted = int(input())

# Изчисляване на общата площ на стените
total_area = 4 * wall_height * wall_width

# Изчисляване на площта, която няма да бъде боядисана
not_painted_area = total_area * percent_not_painted / 100

# Инициализиране на броячите
remaining_area = total_area - not_painted_area
paint_left = 0

# Боядисване на стени
command = input()
while command != "Tired!":
    paint_liters = int(command)
    remaining_area -= paint_liters
    if remaining_area <= 0:
        paint_left = abs(remaining_area)
        remaining_area = 0
        break
    command = input()

# Отпечатване на резултата
if remaining_area > 0:
    print(f"{ceil(remaining_area)} quadratic m left.")
elif paint_left > 0:
    print(f"All walls are painted and you have {paint_left:.0f} l paint left!")
else:
    print("All walls are painted! Great job, Pesho!")
